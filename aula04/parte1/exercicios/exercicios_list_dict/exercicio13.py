# Objetivo: Dado um dicionário de estoque de produtos, filtrar aqueles com quantidade maior que 0.

estoque = [
    {"item": "Camiseta", "codigo": 101, "quantidade": 15},
    {"item": "Calça Jeans", "codigo": 102, "quantidade": 0},
    {"item": "Tênis", "codigo": 103, "quantidade": 30},
    {"item": "Jaqueta", "codigo": 104, "quantidade": 0},
    {"item": "Boné", "codigo": 105, "quantidade": 20},
    {"item": "Meias", "codigo": 106, "quantidade": 50},
    {"item": "Óculos de Sol", "codigo": 107, "quantidade": 0},
    {"item": "Relógio", "codigo": 108, "quantidade": 12},
    {"item": "Mochila", "codigo": 109, "quantidade": 7},
    {"item": "Cinto", "codigo": 110, "quantidade": 0}
]

filtered_estoque = []

for dict in estoque:
    if dict['quantidade'] > 0:
        filtered_estoque.append(dict)

print(filtered_estoque)