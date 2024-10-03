import pandas as pd
from pathlib import Path
from PyPDF2 import PdfReader
import os
import datetime  # Adicione esta linha

class PDFAnalyzer:
    def __init__(self, caminho):
        self.caminho = Path(caminho)

    def lista_pastas_e_arquivos(self):
        if self.caminho.exists():
            pastas_arquivos = []
            self.percorrer_pastas(self.caminho, pastas_arquivos)
            return pastas_arquivos if pastas_arquivos else "Nenhuma pasta ou arquivo encontrado no diretório."
        else:
            return f"O diretório {self.caminho} não foi encontrado."

    def percorrer_pastas(self, pasta, pastas_arquivos):
        for item in pasta.iterdir():
            if item.is_dir():
                self.percorrer_pastas(item, pastas_arquivos)
            else:
                if item.suffix.lower() == '.pdf':
                    quantidade_paginas = self.contar_paginas(item)
                    diretorio = item.parent
                    nome_pasta_antes_do_arquivo = diretorio.parent.name
                    pastas_arquivos.append({'Nome Pasta': nome_pasta_antes_do_arquivo, 'Nome': item.name, 'QTDE DE PAGINAS': quantidade_paginas, 'Caminho': str(item)})
                else:
                    pastas_arquivos.append({'Nome': item.name, 'Caminho': str(item)})

    def contar_paginas(self, item):
        try:
            with open(item, 'rb') as file:
                pdf = PdfReader(file)
                return len(pdf.pages)
        except Exception as e:
            return f'Erro: {e}'

    def salvar_relatorio(self, dados):
        diretorio_relatorios = Path(os.path.dirname(os.path.abspath(__file__))) / 'RELATORIOS'
        diretorio_relatorios.mkdir(parents=True, exist_ok=True)
        arquivo_excel = diretorio_relatorios / f'pastas_arquivos-{self.data()}.xlsx'

        # Apaga o arquivo se já existir
        if arquivo_excel.exists():
            arquivo_excel.unlink()
            print(f"Arquivo {arquivo_excel} existente foi apagado.")

        df_resultados = pd.DataFrame(dados)
        df_resultados.to_excel(arquivo_excel, index=False)

    @staticmethod
    def data():
        return datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
