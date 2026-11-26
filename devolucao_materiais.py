
from datetime import datetime


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
        "estado": "Emprestado"
    },
    {
        "codigo": 3,
        "utilizador": "João",
        "fornecedor": "Zacarias",
        "data_entrega": "15/11/2026",
        "estado": "Emprestado"
    }
]


def procurar_emprestimo(codigo):
    for emprestimo in emprestimos:
        if emprestimo["codigo"] == codigo and emprestimo["estado"] == "Emprestado":
            return emprestimo

    return None


def registar_devolucao(emprestimo, material):
    nome_entregador = input("\nNome de quem está a entregar o material: ")
    fornecedor = input("Nome do fornecedor que recebeu o equipamento: ")

    try:
        data_devolucao = datetime.strptime(
            input("Data da devolução (DD/MM/AAAA): "),
            "%d/%m/%Y"
        )

        emprestimo["entregador"] = nome_entregador
        emprestimo["fornecedor_recebeu"] = fornecedor
        emprestimo["data_devolucao"] = data_devolucao
        emprestimo["estado"] = "Devolvido"

        material["disponivel"] = True

        print("\nDEVOLUÇÃO REGISTADA COM SUCESSO!")
        print("Material:", material["nome"])
        print("Entregador:", nome_entregador)
        print("Fornecedor que recebeu:", fornecedor)
        print("Data da devolução:", data_devolucao.strftime("%d/%m/%Y"))
        print("O MATERIAL ESTÁ AGORA DISPONÍVEL.")

    except ValueError:
        print("\nData inválida! Utilize DD/MM/AAAA.")


def devolucoes():

    print("++++++++++++++++++++++++++++++++++++++")
    print("       BEM-VINDO À LOJA BENTOS")
    print("++++++++++++++++++++++++++++++++++++++")

    while True:

        print("\n++++++++++ MATERIAIS DA LOJA ++++++++++")

        for codigo, material in materiais.items():
            print(codigo, "-", material["nome"])

        codigo = input("\nDigite o código do material a devolver: ")

        if not codigo.isdigit():
            print("\nCódigo inválido!")

        elif int(codigo) not in materiais:
            print("\nO MATERIAL NÃO PERTENCE A ESTA EMPRESA.")

        else:
            codigo = int(codigo)
            material = materiais[codigo]

            if material["disponivel"]:
                print("\nEste material não possui nenhum empréstimo ativo.")

            else:
                emprestimo_encontrado = procurar_emprestimo(codigo)

                if emprestimo_encontrado is None:
                    print("\nRegisto de empréstimo não encontrado!")

                else:
                    registar_devolucao(emprestimo_encontrado, material)

        continuar = input("\nDeseja entregar outro material? (s/n): ").lower()

        if continuar != "s":
            break

    print("\n++++++++++++++++++++++++++++++++++++++")
    print("             FIM DO PROCESSO")
    print("++++++++++++++++++++++++++++++++++++++")
