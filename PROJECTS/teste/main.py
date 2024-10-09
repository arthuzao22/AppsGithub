import tkinter as tk
from view import UserView
from controller import UserController

if __name__ == "__main__":
    root = tk.Tk()
    controller = UserController()
    app = UserView(root, controller)
    root.mainloop()
