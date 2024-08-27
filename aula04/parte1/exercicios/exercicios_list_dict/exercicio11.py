# Objetivo: Dada uma lista de dicionários representando produtos, atualizar o preço de um produto específico.

import random

product_name: list = ['Laptop', 'Smartphone', 'Fone de Ouvido', 'Monitor', 'Teclado']

products_dict_list = []

i = 1
while i <= 5:
    dict = {
        'produto': product_name[i-1],
        'preco': random.uniform(100, 200),
        'quantidade': random.randint(1, 10)
    }

    products_dict_list.append(dict)
    
    i += 1

for dictionary in products_dict_list:
    if dictionary['produto'] == 'Laptop':
        dictionary['preco'] = 777

print(products_dict_list)

