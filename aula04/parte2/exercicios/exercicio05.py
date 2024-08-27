# 5) Escreva uma função que receba um dicionário e retorne uma lista de chaves ordenadas

def order_keys_from_dict_to_a_list(dictionary: dict) -> list:
    ordered_keys_list = []

    for key in dictionary:
        ordered_keys_list.append(key)
    
    ordered_keys_list.sort()

    return ordered_keys_list

dict1 = {
    "name": "Alice",
    "age": 30,
    "city": "New York"
}

result = order_keys_from_dict_to_a_list(dict1)
print(result)



