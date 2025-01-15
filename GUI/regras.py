import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

class Regras(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.setup_window()

    def setup_window(self):
        self.title("Regras")
        self.geometry("800x450")
        self.resizable(False, False)
        self.canvas_width = 800
        self.canvas_height = 450
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def exibir_regras(self):

        self.mainloop()