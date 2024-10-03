import sys
from PyQt5.QtWidgets import QApplication
from views.main_view import MainView
from controllers.pdf_controller import PdfController

def main():
    app = QApplication(sys.argv)
    view = MainView()
    controller = PdfController(view)
    view.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
