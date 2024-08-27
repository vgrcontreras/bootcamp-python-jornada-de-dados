### Exercício 14. Tentativas de Conexão
# Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

max_tentativas = 100

num_tentativa = 1

while num_tentativa <= 100: 
    print(f'Tentativa [{num_tentativa}]: Tentando conexão...')

    num_tentativa += 1

print('Tentativas de conexão execedida')