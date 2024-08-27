import csv 

caminho_arquivo: str = r'C:\Users\vgabriel\github\contreras3991\jornada-de-dados\bootcamp\python\aula04\parte2\exemplo.csv'

arquivo_csv = []

with open(file=caminho_arquivo, mode='r', encoding='utf-8') as arquivo:
    leitor_csv = csv.DictReader(arquivo)

    for linha in leitor_csv:
        arquivo_csv.append(linha)

print(arquivo_csv)