### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

lista = [
    {'idade': 11, 'email': ''},
    {'idade': 18, 'email': ''},
    {'idade': 66, 'email': ''},
    {'idade': 65, 'email': ''}
]

for dados in lista:
    if dados['idade'] in range(18, (65 + 1), 1):
        print('Dados válidos')
    else:
        print('Dados inválidos')