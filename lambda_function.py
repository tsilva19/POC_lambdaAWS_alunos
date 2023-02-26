import sqlite3
import json


def lambda_handler(event, context):
    try:
        # Conecte-se ao banco de dados SQLite
        conn = sqlite3.connect('alunos.db')

        # Crie um cursor para executar a consulta
        cur = conn.cursor()

        # Execute a consulta para selecionar todos os alunos
        cur.execute("SELECT * FROM alunos")

        # Obtenha os resultados da consulta
        results = cur.fetchall()

        # Encerre a conexão com o banco de dados
        conn.close()

        # Verifique se a consulta retornou algum resultado
        if len(results) == 0:
            # Se não houver nenhum resultado, retorne um erro com status
            # code 404
            response = {
                "statusCode": 404,
                "body": "Nenhum aluno encontrado"
            }
        else:
            # Crie um dicionário com os resultados da consulta
            alunos = {}
            for row in results:
                alunos[row[0]] = {"nome": row[1], "idade": row[2]}

            # Retorne os resultados da consulta em formato JSON com status
            # code 200
            response = {
                "statusCode": 200,
                "headers": {
                    "Content-Type": "application/json"
                },
                "body": json.dumps(alunos)
            }

    except Exception as e:
        # Se ocorrer um erro, retorne um erro com status code 500
        response = {
            "statusCode": 500,
            "body": str(e)
        }

    return response
