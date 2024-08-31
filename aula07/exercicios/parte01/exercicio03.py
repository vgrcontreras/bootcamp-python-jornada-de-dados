def contar_valores_distintos_lista(lista: list) -> int:
    return len(set(lista))

lista = [1,1,2,3,4,5,6,7,8,9,10]

print(contar_valores_distintos_lista(lista))