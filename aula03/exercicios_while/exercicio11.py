### Exercício 11. Leitura de Dados até Flag
# Ler dados de entrada até que uma palavra-chave específica ("sair") seja fornecida.

frase = 'Ao encontrar a palavra sair. Essa parte não deveria aparecer'

frase_nova = frase.replace(".","")
lista_palavras = frase_nova.split(" ")

i = 0
while i < len(lista_palavras):
    palavra = lista_palavras[i]
    if palavra == 'sair':
        print('execução interrompida pela palavra sair')
        break  # Interrompe o loop `while` quando a palavra "sair" é encontrada
    print(palavra)
    i += 1  # Incrementa o índice para processar a próxima palavra