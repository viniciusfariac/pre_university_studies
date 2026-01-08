from db import encerra_conexao, configuracao_banco
from notas import pesquisar_id
def media():
    conexao = configuracao_banco()
    cursor = conexao.cursor()

    try:
        aluno_id, materias_id = solicitar_dados(cursor)
        media = calcular_media(cursor, aluno_id, materias_id)

        if media is None:
            print("Nenhuma nota encontrada para essas meterias")
        else:
            print(f"Media: {media}")
    finally:
        encerra_conexao(conexao)
        encerra_conexao(cursor)

def relatorio():
    pass

def solicitar_dados(cursor):
    while True:
        try:
            nome_aluno = input("Nome aluno: ")
            id_aluno = pesquisar_id("alunos", "aluno", nome_aluno, cursor)
            materias = input("Digite as materias, separadas por espaço: ").split()
            materias_id = []
            for materia in materias:
                try:
                    materia_id = pesquisar_id("Materia", "materia", materia, cursor)
                    materias_id.append(materia_id)
                except ValueError as e:
                    print(f"Materia invalida {materia}", e)
                    materia = input("Digite a materia novamente: ")
            return id_aluno, materias_id
        except ValueError as e:
            print("Erro de entrada", e)

def calcular_media(cursor, aluno_id, materias_id):
    query = """
        SELECT AVG(nota)
        FROM nota
        WHERE alunoId = %s
          AND materiaId = ANY(%s)
    """

    cursor.execute(query, (aluno_id, materias_id))
    resultado = cursor.fetchone()
    return resultado[0]