# 1) Escreva uma função que receba uma lista de números e retorne a soma de todos os números.

def sum_list(list: list) -> int:
    return sum(list)

lista: list = [1,2,3,4,5,6,7,8,9,10]

result = sum_list(lista)
print(result)