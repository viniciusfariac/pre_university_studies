from alunos import cadastrar_aluno
from notas import lancar_nota
from notas import media, relatorio_estatistico
def sistema_menu ():
    while True:
        print("""Opções dispóniveis:  
            1- Cadastrar Aluno
            2- Lançar nota
            3- Relátorio estatistico
            4- Ver média
            5- Sair""")
        opcao = input("Digite o que quer fazer")
        opcoes(opcao)

def opcoes (numero):
    match numero:
        case 1:
            return cadastrar_aluno()
        case 2:
            return lancar_nota()
        case 3:
            return relatorio_estatistico()
        case 4:
            return media()
        case 5:
            return sair()
        
def sair():
    return "Obrigado por iniciar nosso sistema", False