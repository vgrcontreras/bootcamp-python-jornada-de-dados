### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

logs = [{'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
        {'timestamp': '2021-06-24 10:00:00', 'level': 'TESTE', 'message': 'Falha na conexão'},
        {'timestamp': '2021-06-24 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
        {'timestamp': '2021-06-24 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
]

for log in logs:
    if log['level'] == 'ERROR':
        print(log)