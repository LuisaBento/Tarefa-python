
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
            emprestimo_encontrado = None

            for emprestimo in emprestimos:
                if emprestimo["codigo"] == codigo and emprestimo["estado"] == "Emprestado":
                    emprestimo_encontrado = emprestimo
                    break

            if emprestimo_encontrado is None:
                print("\nRegisto de empréstimo não encontrado!")

            else:
                nome_entregador = input("\nNome de quem está a entregar o material: ")

                fornecedor = input("Nome do fornecedor que recebeu o equipamento: ")

                try:
                    data_devolucao = datetime.strptime(
                        input("Data da devolução (DD/MM/AAAA): "),
                        "%d/%m/%Y"
                    )

                    emprestimo_encontrado["entregador"] = nome_entregador
                    emprestimo_encontrado["fornecedor_recebeu"] = fornecedor
                    emprestimo_encontrado["data_devolucao"] = data_devolucao
                    emprestimo_encontrado["estado"] = "Devolvido"

                    material["disponivel"] = True

                    print("\nDEVOLUÇÃO REGISTADA COM SUCESSO!")
                    print("Material:", material["nome"])
                    print("Entregador:", nome_entregador)
                    print("Fornecedor que recebeu:", fornecedor)
                    print("Data da devolução:", data_devolucao.strftime("%d/%m/%Y"))
                    print("O MATERIAL ESTÁ AGORA DISPONÍVEL.")

                except ValueError:
                    print("\nData inválida! Utilize DD/MM/AAAA.")

    continuar = input("\nDeseja entregar outro material? (s/n): ").lower()

    if continuar != "s":
        break

print("\n++++++++++++++++++++++++++++++++++++++")
print("             FIM DO PROCESSO")
print("++++++++++++++++++++++++++++++++++++++")
