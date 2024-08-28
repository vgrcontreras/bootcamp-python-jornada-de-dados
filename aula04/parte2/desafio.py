CONSTANTE_BONUS = 1000

# 1) Solicita ao usuário que digite seu nome

def create_json_object_with_bonus_data():
    json_object = {}

    nome_valido: bool = False
    salario_valido: bool = False
    bonus_valido: bool = False

    while nome_valido is not True:
        try:
            nome_usuario: str = input('Digite o seu nome: ')

            if len(nome_usuario) == 0 or nome_usuario.isspace():
                raise ValueError('O nome não pode estar vazio')
            elif any(char.isdigit() for char in nome_usuario):
                raise ValueError('O nome não deve conter digitos')
            else:
                nome_valido: bool = True
                print("Nome válido: ", nome_usuario)
                json_object['nome'] = nome_usuario
        except ValueError as e:
            print(e)

    # 2) Solicita ao usuário que digite o valor do seu salário
    # Converte a entrada para um número de ponto flutuante

    while salario_valido is not True:
        try:
            salario: float = float(input('Digite o seu salário: '))

            if salario <= 0:
                print('Por favor, digite um valor positivo para o salário.')
            else:
                print('Salário válido: ', salario)
                salario_valido: bool = True
                json_object['salario'] = salario
        except ValueError as e:
            print('Você digitou um salário inválido')

    # 3) Solicita ao usuário que digite o valor do bônus recebido
    # Converte a entrada para um número de ponto flutuante
    while bonus_valido is not True:
        try:
            valor_bonus: float = float(input('Digite o percentual do bonus: '))

            if valor_bonus < 0:
                print('Por favor, digite um valor positivo para o salário.')
            else:    
                print('Bonus válido: ', valor_bonus)
                bonus_valido: bool = True
                json_object['percentual_bonus'] = valor_bonus
        except ValueError as e:
            print('Você digitou um valor de bônus invalido')

    # 4) Calcule o valor do bônus final 

    bonus_final: float = CONSTANTE_BONUS + salario * valor_bonus

    json_object['bonus'] = bonus_final

    print(f'Olá {nome_usuario}, o seu bônus foi de {bonus_final}')
    print(f'JSON object criado: {json_object}')

    return json_object

list_of_json_object = []

json_object1 = create_json_object_with_bonus_data()
json_object2 = create_json_object_with_bonus_data()

list_of_json_object.append(json_object1)
list_of_json_object.append(json_object2)

print(list_of_json_object)

