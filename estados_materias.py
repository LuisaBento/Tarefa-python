
print("++++++++++++++++++++++++++++++++++++++")
print("       BEM-VINDO À LOJA BENTOS")
print("++++++++++++++++++++++++++++++++++++++")

equipamentos = {
    1: {
        "nome": "Samsung",
        "disponivel": True
    },
    2: {
        "nome": "Nokia",
        "disponivel": False
    },
    3: {
        "nome": "iPhone",
        "disponivel": True
    },
    4: {
        "nome": "iPad",
        "disponivel": False
    }
}

while True:

    print("\nLISTA DE EQUIPAMENTOS")
    print("----------------------------------------")
    print("CÓDIGO | EQUIPAMENTO")
    print("----------------------------------------")

    for codigo, equipamento in equipamentos.items():
        print(codigo, "|", equipamento["nome"])

    print("----------------------------------------")

    codigo = input("\nDeseja ver o estado de qual equipamento? ")

    if not codigo.isdigit():
        print("\nCódigo inválido!")

    elif int(codigo) not in equipamentos:
        print("\nEquipamento não encontrado!")

    else:
        codigo = int(codigo)

        equipamento = equipamentos[codigo]

        print("\n++++++++++ ESTADO DO EQUIPAMENTO ++++++++++")
        print("Equipamento:", equipamento["nome"])

        if equipamento["disponivel"]:
            print("Estado: Disponível")
        else:
            print("Estado: Não disponível")

    nova_consulta = input(
        "\nDeseja fazer uma nova consulta? (S/N): "
    ).lower()

    if nova_consulta != "s":
        break

print("\n++++++++++++++++++++++++++++++++++++++")
print("             FIM DO PROCESSO")
print("++++++++++++++++++++++++++++++++++++++")
