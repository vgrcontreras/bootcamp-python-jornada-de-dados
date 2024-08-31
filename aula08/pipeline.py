from aula08.etl import pipeline_ler_e_carregar_dados_transformados

path_folder = r'C:\Users\vgabriel\github\contreras3991\jornada-de-dados\bootcamp\python\aula08\data'

pipeline_ler_e_carregar_dados_transformados(caminho_pasta=path_folder, formato_arquivos=['csv', 'parquet'])