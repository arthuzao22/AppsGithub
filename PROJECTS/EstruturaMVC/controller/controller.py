from model.model import PDFAnalyzer
from views.view import PDFAnalyzerView

class PDFAnalyzerController:
    def __init__(self, view):
        self.view = view
        self.view.set_controller(self)

    def ativar_codigo(self):
        entrada_texto = self.view.entrada.get()
        self.view.mostrar_mensagem("Informação", f"URL ativada: {entrada_texto}")
        
        pdf_analyzer = PDFAnalyzer(entrada_texto)
        resultados = pdf_analyzer.lista_pastas_e_arquivos()
        
        if isinstance(resultados, list):
            pdf_analyzer.salvar_relatorio(resultados)
            self.view.mostrar_mensagem("Arquivo salvo em: ", f"RELATORIOS/pastas_arquivos-{pdf_analyzer.data()}.xlsx")
        else:
            self.view.mostrar_mensagem("Resultado", resultados)
