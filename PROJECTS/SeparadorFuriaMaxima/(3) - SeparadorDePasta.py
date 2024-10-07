import os
import shutil
import re  # Importando regex para manipulação de strings

# Defina os diretórios de destino - PROVAS -------------------------------------------------------------------
pasta = r"..\SeparadorFuriaMaxima\CaminhosDosArquivos\ArquivosSeparados"

pasta_principal = r"..\SeparadorFuriaMaxima\pastasSeparadas"
if os.path.exists(pasta_principal):
    # Se existir, remove o diretório e seu conteúdo
    shutil.rmtree(pasta_principal)
    print(f"Diretório existente removido: {pasta_principal}")

caminho_novo_efai_provas = r"..\SeparadorFuriaMaxima\pastasSeparadas\efai\provas"
caminho_novo_efaf_provas = r"..\SeparadorFuriaMaxima\pastasSeparadas\efaf\provas"
caminho_novo_em_provas = r"..\SeparadorFuriaMaxima\pastasSeparadas\em\provas"
caminho_novo_medio_provas = r"..\SeparadorFuriaMaxima\pastasSeparadas\medio\provas"

# Criar as pastas, se não existirem
os.makedirs(caminho_novo_efai_provas, exist_ok=True)
os.makedirs(caminho_novo_efaf_provas, exist_ok=True)
os.makedirs(caminho_novo_em_provas, exist_ok=True)
os.makedirs(caminho_novo_medio_provas, exist_ok=True)

# Defina os diretórios de destino - GABARITO -----------------------------------------------------------------
caminho_novo_efai_gabarito = r"..\SeparadorFuriaMaxima\pastasSeparadas\efai\gabarito"
caminho_novo_efaf_gabarito = r"..\SeparadorFuriaMaxima\pastasSeparadas\efaf\gabarito"
caminho_novo_em_gabarito = r"..\SeparadorFuriaMaxima\pastasSeparadas\em\gabarito"
caminho_novo_medio_gabarito = r"..\SeparadorFuriaMaxima\pastasSeparadas\medio\gabarito"

# Criar as pastas, se não existirem
os.makedirs(caminho_novo_efai_gabarito, exist_ok=True)
os.makedirs(caminho_novo_efaf_gabarito, exist_ok=True)
os.makedirs(caminho_novo_em_gabarito, exist_ok=True)
os.makedirs(caminho_novo_medio_gabarito, exist_ok=True)

# Listar arquivos -------------------------------------------------------------------------------------------
arquivos = os.listdir(pasta)
em = []
efai = []
efaf = []
medio = []

def separador():
    for arquivo in arquivos:
        arquivo_pdf = os.path.join(pasta, arquivo)
        nome_sem_extensao = os.path.splitext(arquivo)[0]
        
        palavras = re.split(r'[_-]', nome_sem_extensao)  # Dividindo por '_' e '-'
        
        # FOI implementada essa função pois no arquivo que foi feita a analise "gabarito" e "Teste" estavam juntas
        #Então caso ocoora isso, é necessaario modificar aqui, ou ate mesmo fazer outra veriuficação 
        for i in range(len(palavras)):
            if 'gabarito' in palavras[i] and 'Teste' in palavras[i]:
                partes = palavras[i].split('-')  # Divide "gabarito-Teste" em ["gabarito", "Teste"]
                palavras[i:i+1] = partes  # Substitui a parte original pela lista resultante

        print(palavras)  # Para verificar a saída

        # Verifica se o arquivo corresponde ao ensino médio
        if 'EM' in palavras:
            if any(x in palavras for x in ['1ª', '2ª', '3ª', '1º', '2º', '3º', '1°', '2°', '3°']):
                if any(x in palavras for x in ['gabarito', 'Gabarito', 'GABARITO', 'gABARITO']):
                    shutil.copy2(arquivo_pdf, caminho_novo_em_gabarito)
                    em.append(arquivo_pdf)
                else:
                    shutil.copy2(arquivo_pdf, caminho_novo_em_provas)
                    em.append(arquivo_pdf)

        # Verifica se o arquivo corresponde ao ensino fundamental I ou II
        elif 'EF' in palavras:
            if any(x in palavras for x in ['1ª', '2ª', '3ª', '4ª', '5ª', '1º', '2º', '3º', '4º', '5º', '1°', '2°', '3°', '4°', '5°']):
                if any(x in palavras for x in ['gabarito', 'Gabarito', 'GABARITO', 'gABARITO']):
                    shutil.copy2(arquivo_pdf, caminho_novo_efai_gabarito)
                    efai.append(arquivo_pdf)
                else:
                    shutil.copy2(arquivo_pdf, caminho_novo_efai_provas)
                    efai.append(arquivo_pdf)
                    
            elif any(x in palavras for x in ['6ª', '7ª', '8ª', '9ª', '6º', '7º', '8º', '9º', '6°', '7°', '8°', '9°']):
                if any(x in palavras for x in ['gabarito', 'Gabarito', 'GABARITO', 'gABARITO']):
                    shutil.copy2(arquivo_pdf, caminho_novo_efaf_gabarito)
                    efaf.append(arquivo_pdf)
                else:
                    shutil.copy2(arquivo_pdf, caminho_novo_efaf_provas)
                    efaf.append(arquivo_pdf)

        # Verifica se o arquivo corresponde ao ensino médio por outro nome
        elif 'médio' in nome_sem_extensao.lower():
            if any(x in palavras for x in ['gabarito', 'Gabarito', 'GABARITO', 'gABARITO']):
                shutil.copy2(arquivo_pdf, caminho_novo_medio_gabarito)
                medio.append(arquivo_pdf)
            else:
                shutil.copy2(arquivo_pdf, caminho_novo_medio_provas)
                medio.append(arquivo_pdf)

# Chama a função separador
separador()
