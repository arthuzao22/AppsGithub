import os
from PyPDF2 import PdfReader, PdfWriter

class FileHandler:
    @staticmethod
    def get_pdf_count():
        return len(os.listdir("../my_app/pdfSeparado"))

    @staticmethod
    def get_pdf_list():
        return os.listdir("../my_app/pdfSeparado")

    @staticmethod
    def read_pdf(index):
        try:
            pdf_path = f'../my_app/pdfSeparado/{index}.pdf'
            reader = PdfReader(pdf_path)
            return reader.pages[0].extract_text()
        except FileNotFoundError:
            print(f"PDF {index} não encontrado.")
            return None

    @staticmethod
    def rename_pdf(index, name, additional_text):
        new_name = f"{additional_text}-{name}.pdf"
        old_path = f'../my_app/pdfSeparado{index}.pdf'
        new_path = os.path.join("../PdfSeparado", new_name)
        os.rename(old_path, new_path)
        return f"Arquivo renomeado para {new_name}"

    @staticmethod
    def clear_folder():
        folder = "../my_app/pdfSeparado"
        for file in os.listdir(folder):
            os.remove(os.path.join(folder, file))
