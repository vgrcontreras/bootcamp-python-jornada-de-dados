# Filtrar Dados Acima de um Limite

def filtrar_acima_de(lista: list, limite: int) -> list:
    resultado = []
    for value in lista:
        if value > limite:
            resultado.append(value)
    
    return resultado

lista = [1,2,3,4,5,6,7,8,9,10]

print(filtrar_acima_de(lista, 5))