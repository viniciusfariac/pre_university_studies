from db import encerra_conexao, configuracao_banco
from notas import solicitar_aluno, solicitar_materia
import psycopg2
from  matplotlib import pyplot as plt
def media():
    conexao = configuracao_banco()
    cursor = conexao.cursor()

    try:
        aluno_id = solicitar_aluno(cursor)
        materia_id = solicitar_materia(cursor)
        media = calcular_media(cursor, aluno_id, materia_id)

        if media is None:
            print("Nenhuma nota encontrada para essas meterias")
        else:
            print(f"Media: {media:.2f}")
    finally:
        encerra_conexao(conexao)
        encerra_conexao(cursor)

def calcular_media(cursor, aluno_id, materias_id):
    query = """
        SELECT AVG(nota)
        FROM nota
        WHERE alunoId = %s
        AND materiaId = %s
    """

    cursor.execute(query, (aluno_id, materias_id))
    resultado = cursor.fetchone()
    return resultado[0]
    
def relatorio():
    conexao = configuracao_banco()
    cursor = conexao.cursor()

    try:
        aluno_id = solicitar_aluno(cursor)
        materia_id = solicitar_materia(cursor)
        notas = buscar_nota_relatorio(cursor, aluno_id, materia_id)
        gerar_grafico(notas)
    finally:
        encerra_conexao(conexao)
        encerra_conexao(cursor)

def buscar_nota_relatorio(cursor, aluno_id, materia_id):
    try:
        query = f"""SELECT nota FROM Nota
        WHERE alunoID = %s
        AND materiaID = %s"""

        cursor.execute(query, (aluno_id, materia_id))

        resultado = cursor.fetchall()
        if resultado is not None:
            return converter_notas(resultado)
        else:
            print("Aluno não tem nota nessa matéria")
    
    except psycopg2.Error as e:
        print("Erro no banco", e)
    finally:
        encerra_conexao(cursor)
    

def converter_notas(raw_notas):
    return [nota[0] for nota in raw_notas]

def gerar_grafico(notas):
    plt.plot(notas, marker='o')
    plt.title("Notas dos alunos")
    plt.xlabel("Avaliações")
    plt.ylabel("Nota")
    plt.ylim(0, 10)
    plt.grid(True)
    plt.show()