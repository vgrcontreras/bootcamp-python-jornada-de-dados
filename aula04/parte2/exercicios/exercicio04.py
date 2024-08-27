# 4) Implemente uma função que receba dois argumentos: uma lista de números e um número. 
#    A função deve retornar todas as combinações de pares na lista que somem ao número dado.

def sum_even_numbers(lista: list, num: int) -> list:
    list_sum_number = []

    for number in lista:
        if number % 2 == 0:
            sum_number = number + num
            list_sum_number.append(sum_number)
    
    return list_sum_number

lista = [1,2,3,4,5,6,7,8,9,10]

result = sum_even_numbers(lista, 1)
print(result)
            