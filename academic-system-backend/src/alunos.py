from db import configuracao_banco, encerra_conexao
from datetime import datetime
import psycopg2
from notas import pesquisar_disponiveis

def cadastrar_aluno():
    try:
        conexao = configuracao_banco()
        cursor = conexao.cursor()
        now = datetime.now()
        nome_aluno = input("Nome aluno: ")
        endereco = input("Endereço: ")
        data_nascimento = solicitar_data()
        curso = solicitar_curso(cursor)
        turma_id = solicitar_turma(cursor)
        


        id_matricula = cadastrar_matricula(turma_id, now, cursor, conexao)

        query = "INSERT INTO alunos (name, endereco, data_nascimento, matriculaID) VALUES (%s, %s, %s, %s)"
        values_alunos = nome_aluno, endereco, data_nascimento, id_matricula
        cursor.execute(query, values_alunos)
        conexao.commit()

    except ValueError as e:
        print("Erro de entrada", e)

    except psycopg2.Error as e:
        print("Erro no banco", e)

    except Exception as e:
        print("Erro inesperado", e)

    finally:
        encerra_conexao(conexao)
        encerra_conexao(cursor)

def cadastrar_matricula(turma, now, cursor, conexao):
    try:
        query = """INSERT INTO Matricula (data_matricula, turmaID) 
        VALUES (%s, %s)
        RETURNING matriculaID"""
        cursor.execute(query, (now, turma))

        id = cursor.fetchone()[0]
        conexao.commit()

        print("Dados inseridos com Sucesso")
        return id
    except ValueError as e:
        print("Erro de entrada", e)
    except psycopg2.Error as e:
        print("Erro no banco", e)
    except Exception as e:
        print("Erro inesperado", e)

def pesquisar_id(tabela, entidade_id, entidade, cursor):
    try:
        query =f"""SELECT {entidade_id}ID
            FROM {tabela}
            WHERE name = %s"""
        
        cursor.execute(query, (entidade, ))
        
        resultado = cursor.fetchone()

        if not resultado:
            raise ValueError
        
        return resultado[0]

    except ValueError as e:
        print("Erro de entrada", e)
    except psycopg2.Error as e:
        print("Erro no banco", e)
    except Exception as e:
        print("Erro inesperado", e)
    

def solicitar_data():
    while True:
        try:
            data_nascimento = input("Digite a data de nascimento do aluno: ")
            data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()
            return data_nascimento
        except ValueError as e:
            print("Data inválida, data deve ser: d-m-y")

def solicitar_curso(cursor):
    while True:
        try:
            curso_nome = input("Digite o curso que o aluno faz parte: ")
            resultado = pesquisar_id("Cursos", "curso", curso_nome, cursor)
            if resultado is not None:
                return resultado
            else:
                print("Cursos disponiveis abaixo: ")
                print(pesquisar_disponiveis("Cursos", "name", cursor))
        except ValueError as e:
            print(" ")

def solicitar_turma (cursor):
    while True:
        try:
            nome_turma = input(f"Digite a turma: ")
            resultado = pesquisar_id("Turma", "turma", nome_turma, cursor)
            if resultado is not None:
                return resultado
            else:
                print("Turmas disponiveis abaixo: ")
                print(pesquisar_disponiveis("Turma", "name", cursor))
        except ValueError as e:
            print(" ")
if __name__ == "__main__":
    cadastrar_aluno()