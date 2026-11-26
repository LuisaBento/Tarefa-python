
from estados_materias import estados
from emprestimos_materiais import emprestimos
from consulta_fornecedor import fornecedores_consulta
from atrasos_materiais import atrasos
from devolucao_materiais import devolucoes


def programa_principal():

    print(".......................................")
    print("        BEM-VINDO À LOJA BENTOS")
    print("........................................")

    while True:

        print("\n.........MENU PRINCIPAL ..........")
        print("1 - consultar estado dos materiais ")
        print("2 - Registar empréstimo")
        print("3 - Consultar fornecedores")
        print("4 - Consultar atrasos")
        print("5 - Registar devolução")
        print("0 - Sair")

        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            estados()

        elif opcao == "2":
          emprestimos()

        elif opcao == "3":
            fornecedores_consulta()

        elif opcao == "4":
            atrasos()

        elif opcao == "5":
            devolucoes()

        elif opcao == "0":
            print("\nObrigado por utilizar o sistema da Loja Bentos!")
            break

        else:
            print("\nOpção inválida! Tente novamente.")


if __name__ == "__main__":
    programa_principal()
