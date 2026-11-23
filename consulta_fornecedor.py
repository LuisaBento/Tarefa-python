
print("++++++++++++++++++++++++++++++++++++++")
print("       BEM-VINDO À LOJA BENTOS")
print("++++++++++++++++++++++++++++++++++++++")

fornecedores = {
    1: "Luisa",
    2: "Zacarias",
    3: "Ruth",
    4: "Amos"
}

emprestimos = [
    {"utilizador": "Ana", "fornecedor": "Luisa", "material": "Samsung"},
    {"utilizador": "João", "fornecedor": "Luisa", "material": "Nokia"},
    {"utilizador": "Maria", "fornecedor": "Zacarias", "material": "iPhone"},
    {"utilizador": "Pedro", "fornecedor": "Ruth", "material": "iPad"}
]

while True:

    print("\n++++++++++ FORNECEDORES CADASTRADOS ++++++++++")

    for codigo, nome in fornecedores.items():
        print(codigo, "-", nome)

    nome_fornecedor = input(
        "\nDigite o nome do fornecedor que deseja consultar: "
    )

    fornecedor_encontrado = ""

    for nome in fornecedores.values():
        if nome.lower() == nome_fornecedor.lower():
            fornecedor_encontrado = nome
            break

    if fornecedor_encontrado == "":
        print("\nEste fornecedor não faz parte da equipa Bentos!")

    else:
        total = 0

        print("\n++++++++++ CONSULTA DE FORNECEDOR ++++++++++")
        print("Fornecedor:", fornecedor_encontrado)

        for emprestimo in emprestimos:

            if emprestimo["fornecedor"].lower() == fornecedor_encontrado.lower():
                total += 1

                print("\nMaterial:", emprestimo["material"])
                print("Utilizador:", emprestimo["utilizador"])

        print("\nTotal de empréstimos autorizados:", total)

    continuar = input(
        "\nDeseja consultar outro fornecedor? (s/n): "
    ).lower()

    if continuar != "s":
        break

print("\n++++++++++++++++++++++++++++++++++++++")
print("             FIM DO PROCESSO")
print("++++++++++++++++++++++++++++++++++++++")
