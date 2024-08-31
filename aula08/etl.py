import pandas as pd
import os 
import glob

def extrair_e_consolidar_arquivos(path_folder: str) -> pd.DataFrame:
    files_list: list = glob.glob(os.path.join(path_folder, '*.json'))
    df_list: pd.DataFrame = [pd.read_json(file) for file in files_list]
    df_contanated: pd.DataFrame = pd.concat(df_list)

    return df_contanated

def transformar_dataframes(df: pd.DataFrame) -> pd.DataFrame:
    df['Total'] = df['Quantidade'] * df['Venda']

    return df

def carregar_dataframes_transformados(df: pd.DataFrame, path_to_save: str, files_format: list):
    for format in files_format:
        if format == 'csv':
            df.to_csv(f'{path_to_save}.csv', index=False)
        if format == 'parquet':
            df.to_parquet(f'{path_to_save}.parquet', index=False)

def pipeline_ler_e_carregar_dados_transformados(caminho_pasta: str, formato_arquivos: list):
    concatenated_dfs = extrair_e_consolidar_arquivos(caminho_pasta)
    transformed_dfs = transformar_dataframes(concatenated_dfs)
    carregar_dataframes_transformados(transformed_dfs, path_to_save=caminho_pasta, files_format=formato_arquivos)


if __name__ == '__main__':
    path_folder = r'C:\Users\vgabriel\github\contreras3991\jornada-de-dados\bootcamp\python\aula08\data'

    pipeline_ler_e_carregar_dados_transformados(caminho_pasta=path_folder, formato_arquivos=['csv', 'parquet'])



