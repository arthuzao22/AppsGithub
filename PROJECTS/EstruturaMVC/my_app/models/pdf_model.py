import re
import pandas as pd
from PyPDF2 import PdfReader

class PdfModel:
    def __init__(self):
        self.texto_adicionado = ""
        self.nomes_armazenados = []

    def load_database(self):
        return pd.read_excel('../BdNomes/NomesCpfsBD.xlsx')

    def find_name_in_content(self, content):
        pattern = r'\b[A-Z]+(?:\s+[A-Z]+)+\b'
        names = re.findall(pattern, content)
        db = self.load_database()
        for name in names:
            if name in db['NOME'].values:
                return name
        return None

    def split_pdf(self, pdf_path):
        reader = PdfReader(pdf_path)
        for page in reader.pages:
            print("Separando página", page)
