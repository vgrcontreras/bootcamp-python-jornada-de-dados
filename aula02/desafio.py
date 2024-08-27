CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome


nome_usuario = input('Digite o seu nome: ')

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

try:
    salario = float(input('Digite o seu salário: '))
except ValueError as e:
    print('Você digitou um salário inválido')

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

try:
    valor_bonus = float(input('Digite o percentual do bonus: '))
except ValueError as e:
    print('Você digitou um valor de bônus invalido')
# 4) Calcule o valor do bônus final 

bonus_final = CONSTANTE_BONUS + salario * valor_bonus

# print(bonus_final)

# 5) Imprime a mensagem personalizada incluindo o nome do usuário e o valor do bonus

print(f'Olá {nome_usuario}, o seu bônus foi de {bonus_final}')


# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?