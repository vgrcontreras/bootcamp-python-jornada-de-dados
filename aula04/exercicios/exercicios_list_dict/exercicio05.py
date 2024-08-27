# 5) Dada a lista ["maçã", "banana", "cereja"] e o dicionário {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}, calcule o preço total da lista de compras.

fruits = ["maçã", "banana", "cereja"]

fruits_dict = {"maçã": 0.45, "banana": 0.30, "cereja": 0.65}

preco = 0

for word, value in fruits_dict.items():
    if word in fruits:
        preco += value

print(preco)
