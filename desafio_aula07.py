from typing import List
import csv

def ler_csv(nome_arquivo: str) -> List[dict]:
    lista_dict: list = []

    with open(file=nome_arquivo, mode='r', encoding='utf-8') as arquivo:
        
        leitor_csv = csv.DictReader(arquivo)

        for linha in leitor_csv:
            lista_dict.append(linha)

    return lista_dict 

def processar_dados(lista_dicionarios: list):
    new_dict = {}

    for dict in lista_dicionarios:
        if dict['Categoria'] not in new_dict:
            new_dict[dict['Categoria']] = [dict]
        else:
            new_dict[dict['Categoria']] += [dict]

    return new_dict

def calcular_vendas_categoria(dados_processados: dict) -> dict:
    vendas_por_categoria = {}

    for categoria, items in dados_processados.items():
        total_vendas = sum((int(item['Quantidade']) * int(item['Venda'])) for item in items) 
        vendas_por_categoria[categoria] = total_vendas
    
    return vendas_por_categoria
        
        


caminho_arquivo = 'vendas.csv'

csv_processado = ler_csv(caminho_arquivo)
dict_processado = processar_dados(csv_processado)
vendas_por_categoria = calcular_vendas_categoria(dict_processado)

print(vendas_por_categoria)

    



# read_csv_result = ler_csv(caminho_arquivo)
# print(processar_dados(read_csv_result))
