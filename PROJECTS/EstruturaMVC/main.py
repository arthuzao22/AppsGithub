import tkinter as tk
from views.view import PDFAnalyzerView
from controller.controller import PDFAnalyzerController

def main():
    root = tk.Tk()
    app_view = PDFAnalyzerView(root)
    PDFAnalyzerController(app_view)
    root.mainloop()

if __name__ == "__main__":
    main()
