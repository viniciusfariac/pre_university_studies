from db import configuracao_banco, encerra_conexao
import psycopg2
def lancar_nota ():
    try:
        conexao = configuracao_banco()
        cursor = conexao.cursor()

        nome_aluno = input("Digite o aluno que vai receber a(s) nota(s): ")
        aluno_id = pesquisar_id("alunos", "aluno", nome_aluno, cursor)

        quantidade_nota = int(input("Digite quantas notas gostaria de colocar: "))
        for i in range(quantidade_nota):
            
            nota = int(input(f"Digite a {i + 1} nota: "))
            if nota < 0 or nota > 10:
                raise print("Nota deve estar entre 0 e 10")

            nome_materia = input(f"Digite a matéria da {i + 1}: ")

            materia_id = pesquisar_id("Materia", "materia", nome_materia, cursor)
            
            print(materia_id, aluno_id)
            query = """INSERT INTO Nota (nota, materiaID, alunoID) VALUES
            (%s, %s, %s)"""

            cursor.execute(query, (nota, materia_id, aluno_id))
        conexao.commit()
        print("Notas lançadas com sucesso")


    except ValueError as e:
        print("Erro de entrada", e)

    except Exception as e:
        print("Erro inesperado", e)    

    except psycopg2.Error as e:
        print("Erro no banco", e)

    finally:
        if cursor:
            encerra_conexao(cursor)
        if conexao:
            encerra_conexao(conexao)
        
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