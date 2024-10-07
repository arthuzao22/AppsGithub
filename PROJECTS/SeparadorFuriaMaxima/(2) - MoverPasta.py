import os
import pandas as pd
import shutil

def PegarBaseDeDados():
    caminhoBanco = r'..\SeparadorFuriaMaxima\CaminhosDosArquivos\BancoDeCaminhos\pastas_arquivos.xlsx'
    if os.path.exists(caminhoBanco):  # Verifica se o arquivo existe
        df = pd.read_excel(caminhoBanco)
        caminhos = df['Caminho'].tolist()  # Converte para lista
        return caminhos
    else:
        return []

def MovedorDePasta(caminhos, caminho_novo):
    if caminhos:
        for caminho in caminhos:
            try:
                # Verifica se o caminho original existe
                if os.path.exists(caminho):
                    # Extrai o nome do arquivo
                    nome_arquivo = os.path.basename(caminho)
                    # Define o novo caminho
                    novo_caminho = os.path.join(caminho_novo, nome_arquivo)
                    # Move o arquivo
                    shutil.copy2(caminho, novo_caminho)
                    print(f"Arquivo {nome_arquivo} movido com sucesso para {caminho_novo}")
                else:
                    print(f"Arquivo não encontrado: {caminho}")
            except Exception as e:
                print(f'Erro ao mover {caminho}: {e}')
    else:
        print("Caminho não encontrado!")

def PegarNovoCaminho():
    caminho_novo = r"..\SeparadorFuriaMaxima\CaminhosDosArquivos\ArquivosSeparados"

    if os.path.exists(caminho_novo):  # Verifica se o diretório existe
        shutil.rmtree(caminho_novo)  # Remove o diretório existente
        print(f'Diretório {caminho_novo} removido.')
    
    os.makedirs(caminho_novo)  # Cria um novo diretório
    print(f'Diretório {caminho_novo} criado.')
    
    return caminho_novo


# Execução das funções
caminhos = PegarBaseDeDados()
caminho_novo = PegarNovoCaminho()

if caminho_novo:
    MovedorDePasta(caminhos, caminho_novo)