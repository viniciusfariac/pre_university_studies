from db import configuracao_banco, encerra_conexao
import psycopg2
def lancar_nota ():
    try:
        conexao = configuracao_banco()
        cursor = conexao.cursor()

        aluno_id = solicitar_aluno(cursor)

        quantidade = int(input("Digite quantas notas gostaria de colocar: "))

        for i in range(quantidade):
            while True:
                nota = socilitar_nota(i)
                materia_id = solicitar_materia(cursor)
                query = """INSERT INTO Nota (nota, materiaID, alunoID) VALUES
                (%s, %s, %s)"""

                cursor.execute(query, (nota, materia_id, aluno_id))
                break

        conexao.commit()
        print("Notas lançadas com sucesso")


    except ValueError as e:
        print("Erro de entrada", e)

    except Exception as e:
        print("Erro inesperado", e)
        conexao.rollback() 

    except psycopg2.Error as e:
        print("Erro no banco", e)

    finally:
        if cursor:
            encerra_conexao(cursor)
        if conexao:
            encerra_conexao(conexao)

def solicitar_aluno (cursor):
    while True:
        nome_aluno = input("Digite o aluno que vai receber a(s) nota(s): ")
        try:
            return pesquisar_id("alunos", "aluno", nome_aluno, cursor)
        except ValueError as e:
            print("Erro de entrada", e)

def solicitar_materia (cursor):
    while True:

        nome_materia = input(f"Digite a matéria: ")

        try:
            return pesquisar_id("Materia", "materia", nome_materia, cursor)
        
        except ValueError as e:
            print("Erro de entrada", e)

def socilitar_nota(i):
    while True:
        try:
            nota = float(input(f"Digite a {i + 1} nota: "))

            if nota < 0 or nota > 10:
                raise ValueError("Nota deve estar entre 0 e 10")
            return nota
        except ValueError as e:
            print("Nota inválida, digite uma nota de 0 a 10")
    
def pesquisar_id(tabela, entidade_id, entidade, cursor):
    try:
        query =f"""SELECT {entidade_id}ID
            FROM {tabela}
            WHERE name = %s"""
        
        cursor.execute(query, (entidade, ))
        
        resultado = cursor.fetchone()

        if not resultado:
            raise ValueError(f"Nome invalido na tabela {tabela}: {entidade}")
        
        return resultado[0]


    except ValueError as e:
        print("Erro de entrada", e)
    except psycopg2.Error as e:
        print("Erro no banco", e)
    except Exception as e:
        print("Erro inesperado", e)