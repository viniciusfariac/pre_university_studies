from db import configuracao_banco, encerra_conexao
def lancar_nota ():
    conexao = configuracao_banco()
    cursor = conexao.cursor()
    quantidade_nota = input("Digite quantas notas gostaria de colocar: ")
    nome_aluno = input("Digite o aluno que vai receber a(s) nota(s): ")
    for i in range(quantidade_nota):
        nota = input(f"Digite a {i - 1} nota: ")
        materia = input(f"Digite a matéria da {i - 1}")

        materia_id = pesquisar_materia(materia, cursor)
        aluno_id = pesquisar_aluno(nome_aluno, cursor)
        

def pesquisar_aluno(nome_aluno, cursor):
    try:
        query ="""SELECT alunoid
            FROM alunos
            WHERE name = %s"""
        
        cursor.execute(query, (nome_aluno, ))
        
        resultado = cursor.fetchone()
        if resultado != None:
            encerra_conexao(cursor)
            return resultado[0]
        else:
            print("Digite o nome de um aluno válido")

    except ValueError as e:
        print(e)

def pesquisar_materia(materia, cursor):
    try:
        query ="""SELECT materiaID
            FROM Materia
            WHERE name = %s"""
        
        cursor.execute(query, (materia, ))
        
        resultado = cursor.fetchone()
        if resultado != None:
            encerra_conexao(cursor)
            return resultado[0]
        else:
            print("Digite o nome de uma matéria válida")

    except ValueError as e:
        print(e)