
from datetime import datetime

print("++++++++++++++++++++++++++++++++++++++")
print("       BEM-VINDO À LOJA BENTOS")
print("++++++++++++++++++++++++++++++++++++++")

materiais = {
    1: {"nome": "Samsung", "disponivel": True},
    2: {"nome": "Nokia", "disponivel": False},
    3: {"nome": "iPhone", "disponivel": False},
    4: {"nome": "iPad", "disponivel": True}
}

emprestimos = [
    {
        "codigo": 2,
        "utilizador": "Ana",
        "fornecedor": "Luisa",
        "data_entrega": "10/11/2026",
        "data_devolucao": "15/11/2026"
    },
    {
        "codigo": 3,
        "utilizador": "João",
        "fornecedor": "Zacarias",
        "data_entrega": "17/11/2026",
        "data_devolucao": "25/11/2026"
    }
]

while True:

    print("\n++++++++++ MATERIAIS CADASTRADOS ++++++++++")

    for codigo, material in materiais.items():
        print(codigo, "-", material["nome"])

    codigo = input("\nDigite o código do material: ")

    if not codigo.isdigit():
        print("\nCódigo inválido!")

    elif int(codigo) not in materiais:
        print("\nMaterial não encontrado!")

    else:
        codigo = int(codigo)
        material = materiais[codigo]

        if material["disponivel"]:
            print("\nEQUIPAMENTO EM STOCK!")

        else:
            for emprestimo in emprestimos:

                if emprestimo["codigo"] == codigo:

                    print("\n++++++++++ DADOS DO EMPRÉSTIMO ++++++++++")
                    print("Material:", material["nome"])
                    print("Utilizador:", emprestimo["utilizador"])
                    print("Fornecedor:", emprestimo["fornecedor"])
                    print("Data de entrega:", emprestimo["data_entrega"])
                    print("Data prevista de devolução:", emprestimo["data_devolucao"])

                    hoje = datetime.today()
                    data_devolucao = datetime.strptime(
                        emprestimo["data_devolucao"],
                        "%d/%m/%Y"
                    )

                    if hoje.date() > data_devolucao.date():
                        print("\nEQUIPAMENTO EM ATRASO!")

                    else:
                        print("\nAGUARDANDO A DATA DE DEVOLUÇÃO.")

                    break

            else:
                print("\nNão existem registos de empréstimo para este material.")

    continuar = input("\nDeseja consultar outro material? (s/n): ").lower()

    if continuar != "s":
        break

print("\n++++++++++++++++++++++++++++++++++++++")
print("             FIM DO PROCESSO")
print("++++++++++++++++++++++++++++++++++++++")
