import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

class Grid:
    def __init__(self):
        self.setup_window()
        self.create_grid()
        self.run()

    def setup_window(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper")
        self.root.geometry("500x800")
        self.root.resizable(False, False)
        self.canvas_width = 400
        self.canvas_height = 600
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def create_grid(self):
        for i in range(10):
            for j in range(10):
                self.canvas.create_rectangle(i * 50, j * 50, (i + 1) * 50, (j + 1) * 50)

    def run(self):
        self.root.mainloop()