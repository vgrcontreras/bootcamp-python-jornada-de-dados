# Objetivo: Dados dois dicionários, fundi-los em um único dicionário.

dict_1: dict = {
    'a': 1,
    'b': 3,
    'c': 2,
    'd': 10
}

dict_2: dict = {
    'e': 1,
    'f': 3,
    'g': 2,
    'h': 10
}

merged_dicts = dict_1 | dict_2

print(merged_dicts)