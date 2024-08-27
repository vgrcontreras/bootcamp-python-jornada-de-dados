# Exemplo que causa TypeError

nome = 'victor'

try:
    resultado = len(nome)
    print(resultado)
except TypeError as e: # utilização de alias no error para capturar mensagem de erro e poder reutiliza-la caso necessário
    print(e) # printando o erro capturado e armazenado no alias 'e'
else:
    print('tudo ocorreu bem')  # else somente será acessado caso o try ocorra normalmente sem erros
finally:
    print('o importante é participar') # o statement finally será acessado independente se o try ocorrer com erro ou sem erro.

"""
Sempre quando criarmos scripts que contenham interação com o usuário, é interessante como pratica utilizar try/except

"""

numero = int(input('Insira um número: '))

if isinstance(numero, int):  # isinstance permitir verificar se um determinado objeto/variável é do tipo esperado
    print('A variavel é um número inteiro')
else:
    print('A variavel não é um número inteiro')


