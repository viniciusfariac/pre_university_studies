from alunos import cadastrar_aluno
from notas import lancar_nota
from notas_calculos import media, relatorio
def sistema_menu ():
    while True:
        try:
            print("""Opções dispóniveis:  
                1- Cadastrar Aluno
                2- Lançar nota
                3- Relátorio estatistico
                4- Ver média
                5- Sair""")
            opcao = int(input("Digite o que quer fazer: "))
            continuar = opcoes(opcao)
            if continuar is False:
                break
        except ValueError as e:
            print("Erro de entrada, digite um valor de 1 a 5")

def opcoes (numero):
    match numero:
        case 1:
            return cadastrar_aluno()
        case 2:
            return lancar_nota()
        case 3:
            return relatorio()
        case 4:
            return media()
        case 5:
            return sair()
        case _:
            print("Opção inválida, digite um número de 1 a 5")
        
def sair():
    return False

if __name__ == "__main__":
    sistema_menu()