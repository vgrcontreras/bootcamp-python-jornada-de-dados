# Objetivo: Dada uma lista de idades, filtrar apenas aquelas que são maiores ou iguais a 18.

number_list: list = list(range(1, 101))


list_over_eighteen = [num for num in number_list if num >= 18]

print(list_over_eighteen)