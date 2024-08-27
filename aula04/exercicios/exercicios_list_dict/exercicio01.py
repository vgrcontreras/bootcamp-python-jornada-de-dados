# 1) Crie uma lista com os números de 1 a 10 e use um loop para imprimir cada número elevado ao quadrado.

lista_num: list = []

for num in range(1,11,1):
    lista_num.append(num ** 2)

print(lista_num)
