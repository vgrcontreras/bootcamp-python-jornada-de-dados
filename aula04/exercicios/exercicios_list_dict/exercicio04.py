# 4) Escreva um programa que conta o número de ocorrências de cada caractere em uma string usando um dicionário.

texto = 'engenharia de dados'

contagem = {}

for caracter in texto:
    if caracter in contagem:
        contagem[caracter] += 1
    else:
        contagem[caracter] = 1 

print(contagem)