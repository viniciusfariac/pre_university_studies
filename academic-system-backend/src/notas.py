from db import configuracao_banco, encerra_conexao
def lancar_nota ():
    conexao = configuracao_banco()
    cursor = conexao.cursor()

    nome_aluno = input("Digite o aluno que vai receber a(s) nota(s): ")
    aluno_id = pesquisar_id("alunos", "aluno", nome_aluno, cursor)

    quantidade_nota = int(input("Digite quantas notas gostaria de colocar: "))
    for i in range(quantidade_nota):
        try:
            nota = input(f"Digite a {i + 1} nota: ")
            nome_materia = input(f"Digite a matéria da {i + 1}: ")

            materia_id = pesquisar_id("Materia", "materia", nome_materia, cursor)
            
            print(materia_id, aluno_id)
            query = """INSERT INTO Nota (nota, materiaID, alunoID) VALUES
            (%s, %s, %s)"""

            cursor.execute(query, (nota, materia_id, aluno_id))
            conexao.commit()

            encerra_conexao(cursor)
            encerra_conexao(conexao)
        except ValueError as e:
            print(e)
        
def pesquisar_id(tabela, entidade_id, entidade, cursor):
    try:
        query =f"""SELECT {entidade_id}ID
            FROM {tabela}
            WHERE name = %s"""
        
        cursor.execute(query, (entidade, ))
        
        resultado = cursor.fetchone()
        print(resultado)

        if resultado != None:
            return resultado[0]
        else:
            print("Nome inválido")


    except ValueError as e:
        print(e)