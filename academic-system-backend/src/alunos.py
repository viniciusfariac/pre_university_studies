def cadastrar_aluno():
    try:
        nome_aluno = input("Digite o nome do aluno: ")
        endereco = input("Digite o endereço do aluno: ")
        data_nascimento = input("Digite a data de nascimento do aluno: ")
    except ValueError:
        pass