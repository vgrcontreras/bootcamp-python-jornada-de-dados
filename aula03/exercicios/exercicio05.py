from datetime import datetime

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

logs_transactions = [
    {'valor': 10.110, 'horario': datetime(year=2024, month=1, day=1, hour=10, minute=11)},
    {'valor': 10.110, 'horario': datetime(year=2024, month=1, day=1, hour=18, minute=1)},
    {'valor': 9.110, 'horario': datetime(year=2024, month=1, day=1, hour=18, minute=0)},
    {'valor': 65, 'horario': datetime(year=2024, month=1, day=1, hour=19, minute=40)}
]

limite_transacao = 10.000
inicio_horario_comercial = datetime(year=2024, month=1, day=1, hour=9, minute=0)
fim_horario_comercial = datetime(year=2024, month=1, day=1, hour=18, minute=0)

for log in logs_transactions:
    if log['valor'] > limite_transacao or (log['horario'] > fim_horario_comercial and log['horario'] < inicio_horario_comercial):
        print('Trasanção suspeita')
    else:
        print('Transação normal')