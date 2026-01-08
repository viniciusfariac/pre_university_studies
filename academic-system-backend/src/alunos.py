from db import configuracao_banco, encerra_conexao
from datetime import datetime
import psycopg2

def cadastrar_aluno():
    try:
        conexao = configuracao_banco()
        cursor = conexao.cursor()
        now = datetime.now()
        nome_aluno, endereco, data_nascimento, turma_id= receber_dados(cursor, conexao)

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

def receber_dados(cursor, conexao):
    while True:
        try:
            nome_aluno = input("Digite o nome do aluno: ")
            endereco = input("Digite o endereço do aluno: ")

            data_nascimento = input("Digite a data de nascimento do aluno: ")
            data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()

            curso_nome = input("Digite o curso que o aluno faz parte: ")
            curso_id = pesquisar_id("Cursos", "curso", curso_nome, cursor)

            turma_nome = input("Digite a turma que o aluno faz parte: ")
            turma_id = pesquisar_id("Turma", "turma", turma_nome, cursor)


            if curso_id and turma_id:
                return nome_aluno, endereco, data_nascimento, turma_id
        except ValueError as e:
            print("Erro de entrada", e)

        except psycopg2.Error as e:
            print("Erro no banco", e)

        except Exception as e:
            print("Erro inesperado", e)


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

        if resultado != None:
            return resultado[0]
        else:
            print(f"Nome inválido na tabela {tabela}")


    except ValueError as e:
        print("Erro de entrada", e)
    except psycopg2.Error as e:
        print("Erro no banco", e)
    except Exception as e:
        print("Erro inesperado", e)

if __name__ == "__main__":
    cadastrar_aluno()