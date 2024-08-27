### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.


nums_list = []

for num in range(1, 11, 1):
    nums_list.append(num)

even_nums_list = []

for num in nums_list:
    if num % 2 == 0:
        even_nums_list.append(num)

print(even_nums_list)