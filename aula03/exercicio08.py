### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

users_data_list = [
    {'nome': 'Victor', 'sobrenome': 'Contreras', 'idade': 31, 'genero': 'Masculino'},
    {'nome': 'Juliana', 'sobrenome': 'Carvalho', 'idade': 24, 'genero': 'Feminino'},
    {'nome': 'Victor', 'sobrenome': None, 'idade': 31, 'genero': None},
    {'nome': 'Victor', 'sobrenome': 'Contreras', None: 31, 'genero': 'Masculino'},
    {'nome': None, 'sobrenome': 'Contreras', 'idade': 31, 'genero': 'Masculino'},
]

for users_data in users_data_list:
    for key, value in users_data.items():
        if value is None:
            print(f'Value for {key} in {users_data} dict is missing')