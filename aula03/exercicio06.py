### Exercício 6. Contagem de Palavras em Textos
# Objetivo:** Dado um texto, contar quantas vezes cada palavra única aparece nele.

text = input('Digite um texto qualquer: ')

novo_texto = text.replace(",", "")
lista_palavras = novo_texto.split(" ")

contagem_palavras = {}

for palavra in lista_palavras:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)
