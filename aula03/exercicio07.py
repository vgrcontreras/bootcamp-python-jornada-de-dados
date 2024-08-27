# ## Exercício 7. Normalização de Dados
# Objetivo:** Normalizar uma lista de números para que fiquem na escala de 0 a 1.

lista = [253, 180, 390.76, 255.98]

min_val = min(lista)
max_val = max(lista)

lista_normalizada = []

for num in lista:
    num_normalized = (num - min_val) / (max_val - min_val)
    lista_normalizada.append(num_normalized)

print(lista_normalizada)