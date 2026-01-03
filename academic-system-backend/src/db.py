from dotenv import load_dotenv
import os
import psycopg2

load_dotenv()

def configuracao_banco ():
    conexao = psycopg2.connect(
        database = os.getenv("DB_NAME"),
        port = os.getenv("DB_PORT"),
        host = os.getenv("DB_HOST"),
        user = os.getenv("DB_USER"),
        password = os.getenv("DB_PASSWORD")
    )
    return conexao

configuracao_banco()