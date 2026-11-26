
from datetime import datetime


materiais = {
    1: {"nome": "Samsung", "disponivel": True},
    2: {"nome": "Nokia", "disponivel": True},
    3: {"nome": "iPhone", "disponivel": False},
    4: {"nome": "iPad", "disponivel": False}
}

registos_emprestimos = []

nome_usuario = ""
nome_fornecedor = ""

def emprestimos():
    global nome_usuario, nome_fornecedor

    print("....................................")
    print("        BEM-VINDO À LOJA BENTOS")
    print("....................................")

    while True:

        print("\n........ MATERIAIS .........")

        for codigo, material in materiais.items():
            print(codigo, "-", material["nome"])

        codigo = input("\nDigite o código do material: ")

        if not codigo.isdigit():
            print("Código inválido!")

        elif int(codigo) not in materiais:
            print("Material não encontrado!")

        else:
            codigo = int(codigo)
            material = materiais[codigo]

            if not material["disponivel"]:
                print("\nMATERIAL NÃO DISPONÍVEL!")

            else:
                print("\nMATERIAL DISPONÍVEL!")

                if nome_usuario == "":
                    nome_usuario = input("Nome do utilizador: ")
                    nome_fornecedor = input("Nome do fornecedor: ")

                registar_emprestimo(codigo, material)

        continuar = input(
            "\nDeseja emprestar mais algum material? (s/n): "
        ).lower()

        if continuar != "s":
            break

    mostrar_resumo()

def registar_emprestimo(codigo, material):
    global nome_usuario, nome_fornecedor

    try:
        data_entrega = datetime.strptime(
            input("Data da entrega (DD/MM/AAAA): "),
            "%d/%m/%Y"
        )

        data_devolucao = datetime.strptime(
            input("Data prevista da devolução (DD/MM/AAAA): "),
            "%d/%m/%Y"
        )

        if data_devolucao < data_entrega:
            print("A data de devolução não pode ser anterior à entrega!")

        else:
            registo = {
                "utilizador": nome_usuario,
                "fornecedor": nome_fornecedor,
                "codigo": codigo,
                "material": material["nome"],
                "data_entrega": data_entrega,
                "data_devolucao": data_devolucao
            }

            registos_emprestimos.append(registo)
            material["disponivel"] = False

            print("\nEMPRÉSTIMO REGISTADO COM SUCESSO!")
            print("Material:", material["nome"])
            print("Código:", codigo)
            print("Utilizador:", nome_usuario)
            print("Fornecedor:", nome_fornecedor)
            print("Data de entrega:", data_entrega.strftime("%d/%m/%Y"))
            print("Data de devolução:", data_devolucao.strftime("%d/%m/%Y"))

    except ValueError:
        print("Data inválida! Utilize DD/MM/AAAA.")


def mostrar_resumo():
    print("\n...................................")
    print("          RESUMO DOS EMPRÉSTIMOS")
    print(".....................................")

    if len(registos_emprestimos) == 0:
        print("Nenhum empréstimo foi realizado.")

    else:
        for registo in registos_emprestimos:
            print("\nMaterial:", registo["material"])
            print("Código:", registo["codigo"])
            print("Utilizador:", registo["utilizador"])
            print("Fornecedor:", registo["fornecedor"])
            print("Data da entrega:", registo["data_entrega"].strftime("%d/%m/%Y"))
            print("Data da devolução:", registo["data_devolucao"].strftime("%d/%m/%Y"))



    print("\n...................................")
    print("               FIM !")
    print(".....................................")


if __name__ == "__main__":
    emprestimos()
