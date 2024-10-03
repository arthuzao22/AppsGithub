from models.pdf_model import PdfModel
from utils.file_handler import FileHandler
from PyQt5.QtWidgets import QFileDialog


class PdfController:
    def __init__(self, view):
        self.model = PdfModel()
        self.view = view
        self.view.setup_buttons(self)

    def add_text(self, text):
        self.model.texto_adicionado = text
        self.view.show_message(f"Texto adicionado: {text}")

    def rename_pdfs(self):
        self.view.clear_table()
        num_pdfs = FileHandler.get_pdf_count()
        for index in range(1, num_pdfs + 1):
            pdf_content = FileHandler.read_pdf(index)
            if pdf_content:
                name = self.model.find_name_in_content(pdf_content)
                if name:
                    renamed_file = FileHandler.rename_pdf(index, name, self.model.texto_adicionado)
                    self.view.update_table(name)
                    print(renamed_file)

    def separate_pdfs(self):
        self.view.clear_table()
        FileHandler.clear_folder()
        pdfs = FileHandler.get_pdf_list()
        print(pdfs)
        for pdf in pdfs:
            self.model.split_pdf(pdf)
        self.view.show_message("PDFs separados com sucesso.")
        
    def choose_pdf(self):
        """Abre o dialogo para escolher um arquivo PDF."""
        options = QFileDialog.Options()
        file_path, _ = QFileDialog.getOpenFileName(self.view, "Escolher PDF", "", "Arquivos PDF (*.pdf)", options=options)
        if file_path:
            self.view.set_pdf_path(file_path)  # Atualiza o campo de texto com o caminho do PDF
