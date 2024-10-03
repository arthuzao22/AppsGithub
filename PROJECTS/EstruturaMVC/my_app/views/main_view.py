from PyQt5.QtWidgets import QMainWindow, QTextBrowser, QLineEdit, QPushButton, QTableWidget, QTableWidgetItem, QMessageBox, QWidget, QVBoxLayout, QHBoxLayout, QFileDialog
from PyQt5.QtCore import Qt

class MainView(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("App Separador PDF - MVC")
        self.setMinimumSize(600, 500)  # Define tamanho mínimo da janela
        self.initUI()
        self.center_window()  # Centraliza a janela ao iniciar

    def initUI(self):
        central_widget = QWidget(self)  # Cria um widget central
        self.setCentralWidget(central_widget)  # Define o widget central para a janela principal
        
        # Layout principal vertical
        layout = QVBoxLayout()

        # Título
        self.textBrowser = QTextBrowser(self)
        self.textBrowser.setHtml("<h1>Separador e Renomeador de PDFs</h1>")
        layout.addWidget(self.textBrowser)

        # Botão para escolher PDF
        self.pushButton_choose_pdf = QPushButton("Escolher PDF", self)
        layout.addWidget(self.pushButton_choose_pdf)

        # Input para exibir o nome do arquivo PDF escolhido
        self.lineEdit_pdf = QLineEdit(self)
        self.lineEdit_pdf.setPlaceholderText("Nenhum PDF selecionado")
        self.lineEdit_pdf.setReadOnly(True)  # Impede que o usuário edite manualmente
        layout.addWidget(self.lineEdit_pdf)

        # Layout horizontal para entrada de texto e botão de adicionar
        input_layout = QHBoxLayout()
        self.lineEdit = QLineEdit(self)
        self.lineEdit.setPlaceholderText("Digite um texto...")  # Placeholder para ajudar o usuário
        input_layout.addWidget(self.lineEdit)

        self.pushButton_add = QPushButton("Adicionar", self)
        input_layout.addWidget(self.pushButton_add)

        layout.addLayout(input_layout)  # Adiciona o layout horizontal ao layout principal

        # Layout horizontal para botões de renomear e separar
        button_layout = QHBoxLayout()
        self.pushButton_rename = QPushButton("Renomear", self)
        button_layout.addWidget(self.pushButton_rename)

        self.pushButton_separate = QPushButton("Separar PDF", self)
        button_layout.addWidget(self.pushButton_separate)

        layout.addLayout(button_layout)  # Adiciona o layout de botões ao layout principal

        # Tabela para exibir os resultados
        self.tableWidget = QTableWidget(self)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setHorizontalHeaderLabels(["Informações Carregadas"])
        self.tableWidget.setMinimumHeight(200)  # Define altura mínima da tabela
        layout.addWidget(self.tableWidget)

        # Aplica o layout ao widget central
        central_widget.setLayout(layout)

    def setup_buttons(self, controller):
        self.pushButton_choose_pdf.clicked.connect(controller.choose_pdf)  # Conecta o botão para escolher PDF
        self.pushButton_add.clicked.connect(lambda: controller.add_text(self.lineEdit.text()))
        self.pushButton_rename.clicked.connect(controller.rename_pdfs)
        self.pushButton_separate.clicked.connect(controller.separate_pdfs)

    def update_table(self, name):
        row_count = self.tableWidget.rowCount()
        self.tableWidget.insertRow(row_count)
        self.tableWidget.setItem(row_count, 0, QTableWidgetItem(name))

    def clear_table(self):
        self.tableWidget.setRowCount(0)

    def show_message(self, message):
        QMessageBox.information(self, "Informação", message)

    def center_window(self):
        """Centraliza a janela na tela."""
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def set_pdf_path(self, path):
        """Atualiza o campo de texto com o caminho do PDF escolhido."""
        self.lineEdit_pdf.setText(path)
