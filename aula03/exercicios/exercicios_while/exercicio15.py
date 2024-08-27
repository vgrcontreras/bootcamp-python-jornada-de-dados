### Exercício 15. Processamento de Dados com Condição de Parada
# Processar itens de uma lista até encontrar um valor específico que indica a parada.

itens = [
    42, 3.14, "Hello", 99, 7.89, "World", 2024, 0.001, "Python",
    -7, 2.718, "Coding", 1024, -3.14159, "ChatGPT", 18, 6.022e23,
    "Data", 0, 9.81
]



i = 0
while i < len(itens):
    palavra = itens[i]
    if palavra == 'Coding':
        print(f'execução interrompida pela palavra {palavra}')
        break  # Interrompe o loop `while` quando a palavra "sair" é encontrada
    print(palavra)
    i += 1  # Incrementa o índice para processar a próxima palavra