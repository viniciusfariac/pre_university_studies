from db import configuracao_banco, encerra_conexao
from datetime import datetime

def cadastrar_aluno():
    try:
        conexao = configuracao_banco()
        cursor = conexao.cursor()
        nome_aluno, endereco, data_nascimento, turma_id, curso_id = receber_dados()
        now = datetime.now()
        id_matricula = cadastrar_matricula(turma_id, now)
        query = "INSERT INTO alunos (name, endereco, data_nascimento, matriculaID) VALUES (%s, %s, %s, %s)"
        values_alunos = nome_aluno, endereco, data_nascimento, id_matricula
        cursor.execute(query, values_alunos)
        conexao.commit()
        encerra_conexao(conexao)
        encerra_conexao(cursor)

    except ValueError:
        pass
def cadastrar_matricula(turma, now):
    try:
        conexao = configuracao_banco()
        cursor = conexao.cursor()
        query = """INSERT INTO Matricula (data_matricula, turmaID) 
        VALUES (%s, %s)
        RETURNING matriculaID"""
        cursor.execute(query, (now, turma))
        id = cursor.fetchone()[0]
        conexao.commit()
        print("Dados inseridos com Sucesso")
        encerra_conexao(conexao)
        encerra_conexao(cursor)
        return id
    except ValueError as e:
        print(f"Erro para cadastrar matricula {e}")

def receber_dados():
    while True:
        try:
            nome_aluno = input("Digite o nome do aluno: ")
            endereco = input("Digite o endereço do aluno: ")

            data_nascimento = input("Digite a data de nascimento do aluno: ")
            data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").date()

            curso_nome = input("Digite o curso que o aluno faz parte: ")
            curso_id = verifica_curso(curso_nome)

            turma_nome = input("Digite a turma que o aluno faz parte: ")
            turma_id = verifica_turma(turma_nome)

            if curso_id and turma_id:
                return nome_aluno, endereco, data_nascimento, turma_id, curso_id
        except ValueError as e:
            print(e)

def verifica_turma(turma):
    try:
        conexao = configuracao_banco()
        cursor = conexao.cursor()
        
        query ="""SELECT turmaID 
            FROM Turma 
            WHERE name = %s"""
        
        cursor.execute(query, (turma, ))
        
        resultado = cursor.fetchone()
        if resultado != None:
            encerra_conexao(cursor)
            encerra_conexao(conexao)
            return resultado[0]
        else:
            print("Digite uma turma válida")

    except ValueError as e:
        print(e)

def verifica_curso(curso):
    try:
        conexao = configuracao_banco()
        cursor = conexao.cursor()

        query = """SELECT cursoID
            FROM Cursos
            WHERE name = %s"""
        
        cursor.execute(query, (curso, ))
        resultado = cursor.fetchone()
        
        if resultado != None:
            encerra_conexao(cursor)
            encerra_conexao(conexao)
            return resultado[0]
        else:
            print("Digite um curso válido")
    except ValueError as e:
        print(e)

cadastrar_aluno()