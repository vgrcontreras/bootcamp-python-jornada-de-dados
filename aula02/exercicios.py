# #### Inteiros (`int`)

# 1. Escreva um programa que soma dois números inteiros inseridos pelo usuário.

# num_1 = float(input('Digite um número: '))
# num_2 = float(input('Digite outro número: '))

# resultado = num_1 + num_2

# print(f'A soma de {num_1} + {num_2} é {resultado}')

# 2. Crie um programa que receba um número do usuário e calcule o resto da divisão desse número por 5.

############ RESOLUÇÃO

# numero = int(input('Digite um número: '))

# resto_divisao = numero % 5

# print(f'O resto da divisão de {numero} é {resto_divisao}')

############ FIM DA RESOLUÇÃO


# 3. Desenvolva um programa que multiplique dois números fornecidos pelo usuário e mostre o resultado.

############ RESOLUÇÃO

# num_1 = int(input('Digite um número: '))
# num_2 = int(input('Digite outro número: '))
# resultado = num_1 * num_2

# print(f'A multiplicação de {num_1} e {num_2} é {resultado}')

############ FIM DA RESOLUÇÃO


# 4. Faça um programa que peça dois números inteiros e imprima a divisão inteira do primeiro pelo segundo.

############ RESOLUÇÃO

# num_1 = int(input('Digite um número inteiro: '))
# num_2 = int(input('Digite outro número inteiro: '))
# resultado = num_1 // num_2

# print(f'A divisão de {num_1} por {num_2} é {resultado}')

############ FIM DA RESOLUÇÃO

# 5. Escreva um programa que calcule o quadrado de um número fornecido pelo usuário.

############ RESOLUÇÃO

# num = int(input('Digite um número: '))
# resultado = num ** 2

# print(f'A raiz quadrada de {num} é {resultado}')

############ FIM DA RESOLUÇÃO


# #### Números de Ponto Flutuante (`float`)

# 6. Escreva um programa que receba dois números flutuantes e realize sua adição.

############ RESOLUÇÃO

# num_1 = float(input('Digite um número: '))
# num_2 = float(input('Digite outro número: '))
# resultado = num_1 + num_2

# print(f'A soma dos números flutuantes {num_1} e {num_2} é {resultado}')

############ FIM DA RESOLUÇÃO


# 7. Crie um programa que calcule a média de dois números flutuantes fornecidos pelo usuário.

############ RESOLUÇÃO

# num_1 = float(input('Digite um número flutuante: '))
# num_2 = float(input('Digite outro número flutuante: '))
# media = (num_1 + num_2) / 2

# print(f'A média da soma de {num_1} + {num_2} é {media}')

############ FIM DA RESOLUÇÃO


# 8. Desenvolva um programa que calcule a potência de um número (base e expoente fornecidos pelo usuário).

############ RESOLUÇÃO

# base = float(input('Digite a base da potenciação: '))
# expoente = int(input('Digite o expoente: '))
# resultado = base ** expoente

# print(f'A potenciação de {base} por {expoente} é {resultado}')

############ FIM DA RESOLUÇÃO


# 9. Faça um programa que converta a temperatura de Celsius para Fahrenheit.

############ RESOLUÇÃO

# temperatura_celsius = int(input('Digite a temperatura celsius: '))
# temperatura_fahrenheit = (temperatura_celsius * 1.8) + 32

# print(f'{temperatura_celsius} graus celsius em fahrenheit é {temperatura_fahrenheit}')

############ FIM DA RESOLUÇÃO

# 10. Escreva um programa que calcule a área de um círculo, recebendo o raio como entrada.

############ RESOLUÇÃO

# raio = float(input('Digite o raio do círculo: '))
# area = 3.1 * (raio ** 2)

# print(f'A area de um círculo com um raio de {raio} é de {area}')

############ FIM DA RESOLUÇÃO


# #### Strings (`str`)

# 11. Escreva um programa que receba uma string do usuário e a converta para maiúsculas.

############ RESOLUÇÃO

# nome = input('Digite o seu nome: ')

# print(f'nome maíusculo: {nome.upper()}')

############ FIM DA RESOLUÇÃO


# 12. Crie um programa que receba o nome completo do usuário e imprima o nome com todas as letras minúsculas.

############ RESOLUÇÃO

# nome_completo = input('Digite o seu nome completo: ')

# print(f'Nome minúsculo: {nome_completo.lower()}')

############ FIM DA RESOLUÇÃO


# 13. Desenvolva um programa que peça ao usuário para inserir uma frase e, em seguida, imprima esta frase sem espaços em branco no início e no final.

############ RESOLUÇÃO

# frase = input('Digite uma frase de sua escolha: ')

# print(f'{frase.strip()}')

############ FIM DA RESOLUÇÃO


# 14. Faça um programa que peça ao usuário para digitar uma data no formato "dd/mm/aaaa" e, em seguida, imprima o dia, o mês e o ano separadamente.

############ RESOLUÇÃO

# data = input('Digite uma data no formato dd/mm/aaaa: ')

# data_separado = data.split('/')

# dia = data_separado[0]
# mes = data_separado[1]
# ano = data_separado[2]

# print(f'dia: {dia}')
# print(f'mes: {mes}')
# print(f'ano: {ano}')

############ FIM DA RESOLUÇÃO


# 15. Escreva um programa que concatene duas strings fornecidas pelo usuário.

############ RESOLUÇÃO

# string_1 = input('Digite uma palavra: ')
# string_2 = input('Digite outra palavra: ')

# concatenated_strings = " ".join([string_1, string_2])

# print(concatenated_strings)

############ FIM DA RESOLUÇÃO


# #### Booleanos (`bool`)

# 16. Escreva um programa que avalie duas expressões booleanas inseridas pelo usuário e retorne o resultado da operação AND entre elas.

# boolean_1 = bool(input('Digte um valor booleano (True ou False): '))
# boolean_2 = bool(input('Digite outro valor (True ou False): '))


# 17. Crie um programa que receba dois valores booleanos do usuário e retorne o resultado da operação OR.
# 18. Desenvolva um programa que peça ao usuário para inserir um valor booleano e, em seguida, inverta esse valor.
# 19. Faça um programa que compare se dois números fornecidos pelo usuário são iguais.

############ RESOLUÇÃO

# num_1 = float(input('Digite um número: '))
# num_2 = float(input('Digite outro número: '))

# if num_1 == num_2:
#     print('Os números digitados são iguais')

############ FIM DA RESOLUÇÃO

# 20. Escreva um programa que verifique se dois números fornecidos pelo usuário são diferentes.

############ RESOLUÇÃO

# num_1 = float(input('Digite um número: '))
# num_2 = float(input('Digite outro número: '))

# if num_1 != num_2:
#     print('Os números digitados são diferentes')

############ FIM DA RESOLUÇÃO

# #### try-except e if

# 21: Conversor de Temperatura
# 22: Verificador de Palíndromo
# 23: Calculadora Simples
# 24: Classificador de Números
# 25: Conversão de Tipo com Validação
