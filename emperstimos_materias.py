
from datetime import datetime

print("++++++++++++++++++++++++++++++++++++++")
print("        BEM-VINDO À LOJA BENTOS")
print("++++++++++++++++++++++++++++++++++++++")

materiais = {
    1: {"nome": "Samsung", "disponivel": True},
    2: {"nome": "Nokia", "disponivel": True},
    3: {"nome": "iPhone", "disponivel": False},
    4: {"nome": "iPad", "disponivel": False}
}

emprestimos = []

nome_usuario = ""
nome_fornecedor = ""

while True:

    print("\n++++++++++ MATERIAIS ++++++++++")

    for codigo, material in materiais.items():

        if material["disponivel"]:
            estado = "Disponível"
        else:
            estado = "Indisponível"

        print(codigo, "-", material["nome"], "-", estado)

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

            try:

                data_entrega = datetime.strptime(
                    input("Data da entrega (LL/MM/BBBB): "),
                    "%d/%m/%Y"
                )

                data_devolucao = datetime.strptime(
                    input("Data prevista da devolução (LL/MM/MMMM): "),
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

                    emprestimos.append(registo)

                    material["disponivel"] = False

                    print("\nEMPRÉSTIMO REGISTADO COM SUCESSO!")
                    print("Material:", material["nome"])
                    print("Código:", codigo)
                    print("Utilizador:", nome_usuario)
                    print("Fornecedor:", nome_fornecedor)

            except ValueError:

                print("Data inválida! Utilize ll/MM/BBBB.")

    continuar = input(
        "\nDeseja emprestar mais algum material? (s/n): "
    ).lower()

    if continuar != "s":
        break


print("\n++++++++++++++++++++++++++++++++++++")
print("          RESUMO DOS EMPRÉSTIMOS")
print("++++++++++++++++++++++++++++++++++++++")

if len(emprestimos) == 0:

    print("Nenhum empréstimo foi realizado.")

else:

    for registo in emprestimos:

        print("\nMaterial:", registo["material"])
        print("Código:", registo["codigo"])
        print("Utilizador:", registo["utilizador"])
        print("Fornecedor:", registo["fornecedor"])
        print("Data da entrega:", registo["data_entrega"].strftime("%d/%m/%Y"))
        print("Data da devolução:", registo["data_devolucao"].strftime("%d/%m/%Y"))

print("\n++++++++++++++++++++++++++++++++++++")
print("               FIM !     ")
print("++++++++++++++++++++++++++++++++++++++")
