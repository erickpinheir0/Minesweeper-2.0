import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas

class MenuPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_background()
        self.run()

    def setup_window(self):
        self.root.title("Menu Principal")
        self.root.geometry("1380x900")
        self.root.resizable(False, False)
        self.canvas_width = 1380
        self.canvas_height = 900
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()


    def setup_background(self):
        try:
            self.background_image = PhotoImage(file="GUI\images\minesweeper_background.png")
            self.background_label = tk.Label(self.root, image=self.background_image)
            self.background_label.place(x=0, y=0, relwidth=1, relheight=1)
        except:
            print("Error loading background image")

    def run(self):
        self.root.mainloop()