materiais = {
    {'id': 1, "nome": "Samsung", "disponivel": True},
    {'id': 2, "nome": "Nokia", "disponivel": False},
    {'id': 3,"nome": "iPhone", "disponivel": False},
    {'id': 4,"nome": "iPad", "disponivel": True}
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


def devolucao_materiais():
 codigo = input("Digite o código: ")
 controle = False
 for material in materiais:
    if codigo == material['id']:
        controle = True
        print('Id encontrado')
 if not controle:
    print('O id não encontrado')

devolucao_materiais()