from datetime import datetime

### Exercício 1: Verificação de Qualidade de Dados
# Você está analisando um conjunto de dados de vendas e precisa garantir 
# que todos os registros tenham valores positivos para `quantidade` e `preço`. 
# Escreva um programa que verifique esses campos e imprima "Dados válidos" se ambos 
# forem positivos ou "Dados inválidos" caso contrário.

# quantidade = int(input('Digite uma quantidade: '))
# preco = float(input('Digite um preço: '))

# if quantidade > 0 and preco > 0.0:
#     print('Dados válidos')
# else:
#     print('Dados inválidos')

# 2) Imagine que você está trabalhando com dados de sensores IoT. Os dados incluem medições de 
# temperatura. Você precisa classificar cada leitura como 'Baixa', 'Normal' ou 'Alta'. Considerando que:

# Temperatura < 18°C é 'Baixa'
# Temperatura >= 18°C e <= 26°C é 'Normal'
# Temperatura > 26°C é 'Alta'

# temperatura = 27

# if temperatura < 18:
#     print('A temperatura está baixa')
# elif temperatura >= 18 and temperatura <= 26:
#     print('A temperatura é media')
# elif temperatura > 26:
#     print('A temperatura está alta')


### Exercício 3: Filtragem de Logs por Severidade
# Você está analisando logs de uma aplicação e precisa filtrar mensagens 
# com severidade 'ERROR'. Dado um registro de log em formato de dicionário 
# como `log = {'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'}`, 
# escreva um programa que imprima a mensagem se a severidade for 'ERROR'.

# logs = [{'timestamp': '2021-06-23 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
#         {'timestamp': '2021-06-24 10:00:00', 'level': 'TESTE', 'message': 'Falha na conexão'},
#         {'timestamp': '2021-06-24 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
#         {'timestamp': '2021-06-24 10:00:00', 'level': 'ERROR', 'message': 'Falha na conexão'},
# ]

# for log in logs:
#     if log['level'] == 'ERROR':
#         print(log)


### Exercício 4: Validação de Dados de Entrada
# Antes de processar os dados de usuários em um sistema de recomendação, 
# você precisa garantir que cada usuário tenha idade entre 18 e 65 anos e tenha 
# fornecido um email válido. Escreva um programa que valide essas condições 
# e imprima "Dados de usuário válidos" ou o erro específico encontrado.

# lista = [
#     {'idade': 11, 'email': ''},
#     {'idade': 18, 'email': ''},
#     {'idade': 66, 'email': ''},
#     {'idade': 65, 'email': ''}
# ]

# for dados in lista:
#     if dados['idade'] in range(18, (65 + 1), 1):
#         print('Dados válidos')
#     else:
#         print('Dados inválidos')

### Exercício 5: Detecção de Anomalias em Dados de Transações
# Você está trabalhando em um sistema de detecção de fraude e precisa identificar 
# transações suspeitas. Uma transação é considerada suspeita se o valor for superior 
# a R$ 10.000 ou se ocorrer fora do horário comercial (antes das 9h ou depois das 18h). 
# Dada uma transação como `transacao = {'valor': 12000, 'hora': 20}`, verifique se ela é suspeita.

# logs_transactions = [
#     {'valor': 10.110, 'horario': datetime(year=2024, month=1, day=1, hour=10, minute=11)},
#     {'valor': 10.110, 'horario': datetime(year=2024, month=1, day=1, hour=18, minute=1)},
#     {'valor': 9.110, 'horario': datetime(year=2024, month=1, day=1, hour=18, minute=0)},
#     {'valor': 65, 'horario': datetime(year=2024, month=1, day=1, hour=19, minute=40)}
# ]

# limite_transacao = 10.000
# inicio_horario_comercial = datetime(year=2024, month=1, day=1, hour=9, minute=0)
# fim_horario_comercial = datetime(year=2024, month=1, day=1, hour=18, minute=0)

# for log in logs_transactions:
#     if log['valor'] > limite_transacao or (log['horario'] > fim_horario_comercial and log['horario'] < inicio_horario_comercial):
#         print('Trasanção suspeita')
#     else:
#         print('Transação normal')

### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

# text = input('Digite um texto qualquer: ')

# lista_palavras = text.split(" ")

# contagem_palavras = {}

# for palavra in lista_palavras:
#     if palavra in contagem_palavras:
#         contagem_palavras[palavra] += 1
#     else:
#         contagem_palavras[palavra] = 1

# print(contagem_palavras)

# ## Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

# lista = [253, 180, 390.76, 255.98]

# min_val = min(lista)
# max_val = max(lista)

# lista_normalizada = []

# for num in lista:
#     num_normalized = (num - min_val) / (max_val - min_val)
#     lista_normalizada.append(num_normalized)

# print(lista_normalizada)

### Exercício 8. Filtragem de Dados Faltantes
# Objetivo:** Dada uma lista de dicionários representando dados de usuários, filtrar aqueles que têm um campo específico faltando

# users_data_list = [
#     {'nome': 'Victor', 'sobrenome': 'Contreras', 'idade': 31, 'genero': 'Masculino'},
#     {'nome': 'Juliana', 'sobrenome': 'Carvalho', 'idade': 24, 'genero': 'Feminino'},
#     {'nome': 'Victor', 'sobrenome': None, 'idade': 31, 'genero': None},
#     {'nome': 'Victor', 'sobrenome': 'Contreras', None: 31, 'genero': 'Masculino'},
#     {'nome': None, 'sobrenome': 'Contreras', 'idade': 31, 'genero': 'Masculino'},
# ]

# for users_data in users_data_list:
#     for key, value in users_data.items():
#         if value is None:
#             print(f'Value for {key} in {users_data} dict is missing')

### Exercício 9. Extração de Subconjuntos de Dados
# Objetivo:** Dada uma lista de números, extrair apenas aqueles que são pares.


# nums_list = []

# for num in range(1, 11, 1):
#     nums_list.append(num)

# even_nums_list = []

# for num in nums_list:
#     if num % 2 == 0:
#         even_nums_list.append(num)

# print(even_nums_list)


### Exercício 10. Agregação de Dados por Categoria
# Objetivo:** Dado um conjunto de registros de vendas, calcular o total de vendas por categoria.



### Exercícios com WHILE

### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

# frase = 'Ao encontrar a palavra sair. Essa parte não deveria aparecer'

# frase_nova = frase.replace(".","")
# lista_palavras = frase_nova.split(" ")

# i = 0
# while i < len(lista_palavras):
#     palavra = lista_palavras[i]
#     if palavra == 'sair':
#         print('execução interrompida pela palavra sair')
#         break  # Interrompe o loop `while` quando a palavra "sair" é encontrada
#     print(palavra)
#     i += 1  # Incrementa o índice para processar a próxima palavra

### Exercício 12. Validação de Entrada
# Solicitar ao usuário um número dentro de um intervalo específico até que a entrada seja válida.

### Exercício 13. Consumo de API Simulado
# Simular o consumo de uma API paginada, onde cada "página" de dados é processada em loop até que não haja mais páginas.


# ### Exercício 14. Tentativas de Conexão
# # Simular tentativas de reconexão a um serviço com um limite máximo de tentativas.

# max_tentativas = 100

# num_tentativa = 1

# while num_tentativa <= 100: 
#     print(f'Tentativa [{num_tentativa}]: Tentando conexão...')

#     num_tentativa += 1

# print('Tentativas de conexão execedida')

# ### Exercício 15. Processamento de Dados com Condição de Parada
# # Processar itens de uma lista até encontrar um valor específico que indica a parada.

# itens = [
#     42, 3.14, "Hello", 99, 7.89, "World", 2024, 0.001, "Python",
#     -7, 2.718, "Coding", 1024, -3.14159, "ChatGPT", 18, 6.022e23,
#     "Data", 0, 9.81
# ]



# i = 0
# while i < len(itens):
#     palavra = itens[i]
#     if palavra == 'Coding':
#         print(f'execução interrompida pela palavra {palavra}')
#         break  # Interrompe o loop `while` quando a palavra "sair" é encontrada
#     print(palavra)
#     i += 1  # Incrementa o índice para processar a próxima palavra