import sys
from PyQt5.QtWidgets import QFileDialog, QApplication, QMainWindow, QTextBrowser, QLabel, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QStatusBar, QMessageBox, QDesktopWidget
from PyPDF2 import PdfReader, PdfWriter
from PyQt5.QtCore import Qt
import os
import PyPDF2
import re
import pandas as pd
import datetime

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App separador PDF - Tuts")
        self.setGeometry(0, 0, 571, 480)
        self.center_window()  # Centraliza a janela
        self.initUI()
        self.texto_adicionado = ""  # Inicializa o atributo
        self.nomes_armazenados = []
        
        
    def center_window(self):
        # Obtenha a geometria da tela disponível
        screen_geometry = QDesktopWidget().availableGeometry()
        window_geometry = self.frameGeometry()

        # Calcula o centro da tela
        screen_center = screen_geometry.center()

        # Move o centro da janela para o centro da tela
        window_geometry.moveCenter(screen_center)

        # Mova a janela para essa posição
        self.move(window_geometry.topLeft())

    def initUI(self):
        # Texto superior
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setGeometry(10, 0, 551, 41)
        self.textBrowser.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:16pt; font-weight:696; color:#000000;">Separador e renomeador de PDF</span></p></body></html>""")

        # Descrição
        self.textBrowser_2 = QTextBrowser(self)
        self.textBrowser_2.setGeometry(10, 40, 551, 111)
        self.textBrowser_2.setHtml("""<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'MS Shell Dlg 2'; font-size:8.25pt; font-weight:400; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:8pt;">Este aplicativo automatiza o processamento de arquivos PDF, realizando as seguintes etapas:</span></p>
<ol style="margin-top: 0px; margin-bottom: 0px; margin-left: 0px; margin-right: 0px; -qt-list-indent: 1;">
<li style=" font-size:8pt; margin-top:12px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">Leitura de PDFs</span>: Abre os arquivos PDF da pasta <span style=" font-family:'Courier New';">PdfSeparado</span>, extrai o texto da primeira página e encontra nomes em caixa alta utilizando uma expressão regular.</li>
<li style=" font-size:8pt; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">Verificação de nomes</span>: Compara os nomes extraídos com uma base de dados de nomes e CPFs armazenada em um arquivo Excel.</li>
<li style=" font-size:8pt; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">Renomeação de arquivos</span>: Se um nome correspondente for encontrado, o arquivo PDF é renomeado usando a data atual e o nome da pessoa.</li>
<li style=" font-size:8pt; margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-weight:600;">Automatização em massa</span>: O processo é repetido para todos os PDFs na pasta <span style=" font-family:'Courier New';">PdfSeparado</span>.</li></ol>
<p style=" margin-top:0px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;">
<span style=" font-size:8pt;">O objetivo é processar os PDFs, identificar nomes, e renomear os arquivos conforme os dados da base.</span></p></body></html>""")

        # Input de texto
        self.label = QLabel("Informe o texto adicional:", self)
        self.label.setGeometry(20, 170, 201, 16)
        self.label.setStyleSheet("font-size: 12pt;")

        self.lineEdit = QLineEdit(self)
        self.lineEdit.setGeometry(210, 170, 161, 20)

        # Botões
        self.pushButton = QPushButton("Adicionar", self)
        self.pushButton.setGeometry(390, 170, 161, 23)
        self.pushButton.setStyleSheet("font-weight: bold; background-color: #00C957;")
        self.pushButton.clicked.connect(self.on_adicionar_click)  # Conectar ao evento
        self.pushButton.setCursor(Qt.PointingHandCursor)


        self.pushButton_2 = QPushButton("3 - Renomear", self)
        self.pushButton_2.setGeometry(450, 220, 101, 23)
        self.pushButton_2.setStyleSheet("font-weight: bold; background-color: #1E90FF")
        self.pushButton_2.clicked.connect(self.on_renomear_click)  # Conectar ao evento
        self.pushButton_2.setCursor(Qt.PointingHandCursor)


        self.pushButton_3 = QPushButton("2 - Separar PDF", self)
        self.pushButton_3.setGeometry(240, 220, 191, 23)
        self.pushButton_3.setStyleSheet("font-weight: bold; background-color: #1E90FF")
        self.pushButton_3.clicked.connect(self.on_separar_click)  # Conectar ao evento
        self.pushButton_3.setCursor(Qt.PointingHandCursor)


        self.pushButton_4 = QPushButton("1 - Buscar PDF", self)
        self.pushButton_4.setGeometry(20, 220, 191, 23)
        self.pushButton_4.setStyleSheet("font-weight: bold; background-color: #1E90FF")
        self.pushButton_4.clicked.connect(self.on_buscar_pdf_click)  # Conectar ao evento
        self.pushButton_4.setCursor(Qt.PointingHandCursor)


        # Tabela
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setGeometry(15, 260, 541, 171)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["Carregando Informações"])
        # Estilizando a tabela
        self.tableWidget.setStyleSheet("""
            QTableWidget {
                background-color: #ffffff;
                border: 1px solid #dcdcdc;
                font-size: 12px;
                border-color: black;
            }

            QHeaderView::section {
                background-color: #f0f0f0;
                color: #000000;
                font-weight: normal;
                padding: 4px;
                border: 1px solid #dcdcdc;
'                border-color: black;
'            }

            QTableWidget::item {
                border: 1px solid #dcdcdc;
                padding: 4px;
            }

            QTableWidget::item:selected {
                background-color: #87CEFA;
                color: #000000;
            }
        """)

        # Ajustar a largura da coluna para ocupar o espaço disponível
        self.tableWidget.horizontalHeader().setStretchLastSection(True)

#---------------------------------------------------------------------------------------------------------

    def update_table(self):
        self.tableWidget.setRowCount(len(self.nomes_armazenados))
        for i, nome in enumerate(self.nomes_armazenados):
            item = QTableWidgetItem(nome)
            self.tableWidget.setItem(i, 0, item)

    # Função para o botão "Adicionar"
    def on_adicionar_click(self):
        if self.texto_adicionado is None:
            self.texto_adicionado = " "
        self.texto_adicionado = self.lineEdit.text()  # Armazena o texto da linha de entrada
        QMessageBox.information(self, "Informação", f"Texto adicionado ao arquivo: {self.texto_adicionado}")

    # Função para o botão "Renomear PDF"
    def on_renomear_click(self):
        QMessageBox.information(self, "Renomear", "Função para renomear PDF ativada!")
        self.nomes_armazenados.clear() #SERVE PARA LIMPAR O VETOR 

        def LerDados():
            """Lê o banco de dados de nomes e CPFs."""
            caminhoBanco = r'..\PROJECT03\BdNomes\NomesCpfsBD.xlsx'
            lerBancoDeDados = pd.read_excel(caminhoBanco)

            return lerBancoDeDados

        def data():
            agora = datetime.datetime.now()
            return agora.strftime('%m')

        def abrir_pdf(arquivo_pdf):
            """Abre o arquivo PDF para leitura binária e retorna o conteúdo da primeira página."""
            try:
                with open(arquivo_pdf, 'rb') as arquivopdf:
                    # Criar um leitor de PDF
                    pdf = PyPDF2.PdfReader(arquivopdf)

                    # Acessar a primeira página do PDF
                    pagina = pdf.pages[0]

                    # Extrair o texto da página
                    conteudo = pagina.extract_text()

                return conteudo
            except FileNotFoundError:
                print(f"Arquivo não encontrado: {arquivo_pdf}")
                return None

        def encontrar_nomes(conteudo):
            """Encontra nomes em caixa alta sem acentuação em um texto."""
            # Expressão regular para encontrar nomes (palavras em maiúsculas sem acentuação)
            pattern_nomes = r'\b[A-Z]+(?:\s+[A-Z]+)+\b'

            # Encontrar nomes
            nomes_encontrados = re.findall(pattern_nomes, conteudo) if conteudo else []

            return nomes_encontrados

        def verificar_nomes_com_banco(nomes_encontrados, banco_dados):
            """Verifica se os nomes encontrados correspondem a algum nome na lista de CPFs e nomes."""
            try:
                for nome in nomes_encontrados:
                    for index, row in banco_dados.iterrows():
                        if nome == row['NOME']:
                            return row['NOME']
                return None    
            except:
                return "verificar_nomes_com_banco não esta funcionando."

        def QtdeNomesDosArquivosNaPastaPdfSeparado():
            nomes_arquivos = os.listdir("../PROJECT03/PdfSeparado")
            qtde_arquivos = len(nomes_arquivos)

            return qtde_arquivos

        def NomesDosArquivosNaPastaPdfSeparado():
            nomes_arquivos = os.listdir("../PROJECT03/PdfSeparado")

            return nomes_arquivos

        def CaminhoDoDiretorio():
            caminho = f"../PROJECT03/PdfSeparado"
            return caminho

        def RenomearArquivoGeradoPeloLerPdf(caminho_pdf, nome, dt):
            """Renomeia o arquivo PDF com base no nome encontrado."""
            nomeInput = self.texto_adicionado
                
            try:
                novo_nome = f"{dt}-{nomeInput}-{nome}.pdf"
                caminho_novo = os.path.join(CaminhoDoDiretorio(), novo_nome)
                os.rename(caminho_pdf, caminho_novo)

                return f"Arquivo renomeado para: {caminho_novo}"
            except:
                return "NOME não encontrado para renomeação."

        def main(cont):
            # Caminho do arquivo PDF a ser lido
            caminho_pdf = f'../PROJECT03/PdfSeparado/{cont}.pdf'

            # Abrir o PDF e extrair o conteúdo
            conteudo = abrir_pdf(caminho_pdf)

            if conteudo is not None:
                # Encontrar nomes no conteúdo extraído
                nomes_encontrados = encontrar_nomes(conteudo)
                #print(nomes_encontrados)                

                # Carregar dados de nomes e CPFs
                banco_dados = LerDados()
                dt = data()

                # Verificar se algum nome corresponde ao banco de dados
                nome = verificar_nomes_com_banco(nomes_encontrados, banco_dados)
                #print(nome) 

                # Renomear o arquivo conforme o banco de dados
                alertNomesRenomeados = RenomearArquivoGeradoPeloLerPdf(caminho_pdf, nome, dt)
                print(alertNomesRenomeados)
                self.nomes_armazenados.append(nome)
                self.update_table()

        # CHAMA O MAIN
        cont = 1
        for i in range(QtdeNomesDosArquivosNaPastaPdfSeparado()):
            print(f"Processando arquivo {cont}.pdf...")
            main(cont)
            cont += 1

    # Função para o botão "Separar PDF"
    def on_separar_click(self):
        QMessageBox.information(self, "Separar", "Função para Separar PDF ativada!")
        self.nomes_armazenados.clear() #SERVE PARA LIMPAR O VETOR 

        def limpar_pasta(pasta_destino):
            for item in os.listdir(pasta_destino):
                caminho_item = os.path.join(pasta_destino, item)
                if os.path.isfile(caminho_item):
                    os.remove(caminho_item)


        # Função para separar as páginas de um PDF
        def separar_paginas_pdf(caminho_arquivo):
            # Verifica se o arquivo existe
            if not os.path.exists(caminho_arquivo):
                print(f"Arquivo não encontrado: {caminho_arquivo}")
                return

            # Lê o PDF
            with open(caminho_arquivo, 'rb') as f:
                leitor_pdf = PdfReader(f)
                total_paginas = len(leitor_pdf.pages)

                # Define o diretório de destino
                pasta_destino = r"..\PROJECT03\PdfSeparado"

                # Cria o diretório se ele não existir
                if not os.path.exists(pasta_destino):
                    os.makedirs(pasta_destino)
                else:
                    # Limpa a pasta se ela já existir
                    limpar_pasta(pasta_destino)

                # Para cada página do PDF, salva-a como um novo arquivo
                for numero_pagina in range(total_paginas):
                    escritor_pdf = PdfWriter()
                    pagina = leitor_pdf.pages[numero_pagina]
                    escritor_pdf.add_page(pagina)

                    # Define o nome e caminho do novo arquivo PDF
                    nome_pagina = f'{numero_pagina + 1}.pdf'
                    caminho_para_salvar_pdf = os.path.join(pasta_destino, nome_pagina)

                    # Salva a página como um novo arquivo PDF
                    with open(caminho_para_salvar_pdf, 'wb') as nova_pagina:
                        escritor_pdf.write(nova_pagina)

                    self.nomes_armazenados.append(f"Página {numero_pagina + 1} salva como {caminho_para_salvar_pdf}")
                    self.update_table()

        # Exemplo de uso com um arquivo local
        caminho_pdf_url = self.pdf_files
        caminho_arquivo_pdf = caminho_pdf_url

        # Separa as páginas do PDF
        separar_paginas_pdf(caminho_arquivo_pdf)

    # Função para o botão "Sair"
    def on_buscar_pdf_click(self):
        file_name, _ = QFileDialog.getOpenFileName(self, "Selecionar Arquivo PDF", "", "Arquivos PDF (*.pdf)")
        # Abre uma caixa de diálogo para o usuário selecionar um arquivo PDF
        if file_name:
            # Armazena o caminho do arquivo PDF selecionado
            self.pdf_files = file_name
            print("Arquivo PDF selecionado:", self.pdf_files)

        return self.pdf_files


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
