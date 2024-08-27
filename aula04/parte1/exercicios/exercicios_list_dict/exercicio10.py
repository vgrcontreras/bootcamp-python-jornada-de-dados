# Objetivo: Dada uma lista de valores, dividir em duas listas: uma para valores pares e outra para ímpares.

num_list: list = [12,5,654,123,530942,11,24,61,778,1235,3295182,213,214055,2421,140]

even_nums_list: list = []
odd_nums_list: list = []

for num in num_list:
    if num % 2 ==0:
        even_nums_list.append(num)
    else:
        odd_nums_list.append(num)

print(even_nums_list)
print(odd_nums_list)