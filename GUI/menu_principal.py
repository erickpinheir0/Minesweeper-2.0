import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas
from GUI.interface import Grid
from GUI.regras import Regras

class MenuPrincipal:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_window()
        self.setup_background()
        self.images_definition()
        self.images_moving()
        self.create_buttons()
        self.run()

    def setup_window(self):
        self.root.title("Menu Principal")
        self.root.geometry("800x450")
        self.root.resizable(False, False)
        self.canvas_width = 800
        self.canvas_height = 450
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()


    def setup_background(self):
        try:
            self.background_image = PhotoImage(file="GUI/images/minesweeper_background.png")
            # Exibir a imagem no Canvas
            self.canvas.create_image(0, 0, image=self.background_image, anchor=tk.NW)
        except:
            print("Error loading background image")

    def images_definition(self):
        try:
            self.bomba_image = PhotoImage(file="GUI/images/bomba.png")
            self.bandeira_image = PhotoImage(file="GUI/images/bandeira.png")
            self.bandeira_imageID1 = self.canvas.create_image(5, 5, image=self.bandeira_image, anchor=tk.NW)
            self.bandeira_imageID2 = self.canvas.create_image(50, 5, image=self.bandeira_image, anchor=tk.NW)
            self.bomba_imageID1 = self.canvas.create_image(750, 400, image=self.bomba_image, anchor=tk.NW)
            self.bomba_imageID2 = self.canvas.create_image(375, 200, image=self.bomba_image, anchor=tk.NW)

            self.DXBandeiraID1 = 10
            self.DYBandeiraID1 = 10

            self.DXBandeiraID2 = 10
            self.DYBandeiraID2 = 3

            self.DXBombaID1 = 10
            self.DYBombaID1 = 10

            self.DXBombaID2 = 3
            self.DYBombaID2 = 10
        except:
            print("Error loading image")

        self.images_moving()

    def images_moving(self):
        x1A1, y1A1, x2A1, y2A1 = self.canvas.bbox(self.bomba_imageID1)
        x1A2, y1A2, x2A2, y2A2 = self.canvas.bbox(self.bomba_imageID2)
        x1B1, y1B1, x2B1, y2B1 = self.canvas.bbox(self.bandeira_imageID1)
        x1B2, y1B2, x2B2, y2B2 = self.canvas.bbox(self.bandeira_imageID2)

        # Verificar colisões com as bordas
        if x1A1 <= 0 or x2A1 >= self.canvas_width:  # Colisão horizontal
            self.DXBombaID1 = -self.DXBombaID1
        if y1A1 <= 0 or y2A1 >= self.canvas_height:  # Colisão vertical
            self.DYBombaID1 = -self.DYBombaID1

        if x1A2 <= 0 or x2A2 >= self.canvas_width:  # Colisão horizontal
            self.DXBombaID2 = -self.DXBombaID2
        if y1A2 <= 0 or y2A2 >= self.canvas_height:  # Colisão vertical
            self.DYBombaID2 = -self.DYBombaID2

        if x1B1 <= 0 or x2B1 >= self.canvas_width:  # Colisão horizontal
            self.DXBandeiraID1 = -self.DXBandeiraID1
        if y1B1 <= 0 or y2B1 >= self.canvas_height:  # Colisão vertical
            self.DYBandeiraID1 = -self.DYBandeiraID1

        if x1B2 <= 0 or x2B2 >= self.canvas_width:  # Colisão horizontal
            self.DXBandeiraID2 = -self.DXBandeiraID2
        if y1B2 <= 0 or y2B2 >= self.canvas_height:  # Colisão vertical
            self.DYBandeiraID2 = -self.DYBandeiraID2

        self.canvas.move(self.bomba_imageID1, self.DXBombaID1, self.DYBombaID1)
        self.canvas.move(self.bomba_imageID2, self.DXBombaID2, self.DYBombaID2)
        self.canvas.move(self.bandeira_imageID1, self.DXBandeiraID1, self.DYBandeiraID1)
        self.canvas.move(self.bandeira_imageID2, self.DXBandeiraID2, self.DYBandeiraID2)
        self.canvas.tag_raise(self.bomba_imageID1)
        self.canvas.tag_raise(self.bandeira_imageID1)
        self.root.after(65, self.images_moving)

    def create_buttons(self):
        label = tk.Label(self.root, 
        text="MINESWEEPER 2.0", 
        font=("Impact", 25, "italic"), 
        bg="gray", 
        fg="black")
        label.place(relx=0.5, rely=0.13, relwidth=0.45, relheight=0.18, anchor='center')

        fonts_buttons = ("Impact", 15, "italic")

        bombs = tk.Label(self.root, text="💣💣💣💣💣💣", font=("Arial", 25), bg="gray", fg="black")
        bombs.place(relx=0.5, rely=0.23, relwidth=0.3, relheight=0.1, anchor='center')

        button_jogar = tk.Button(self.root, text="Jogar🚩", font=fonts_buttons, bg="gray", fg="black", command=lambda: self.game_initialization())
        button_jogar.place(relx=0.5, rely=0.5, relwidth=0.3, relheight=0.1, anchor='center')

        self.button_regras = tk.Button(self.root, text="Regras🚩", font=fonts_buttons, bg="gray", fg="black", command=lambda: self.mostrar_regras())
        self.button_regras.place(relx=0.5, rely=0.6, relwidth=0.3, relheight=0.1, anchor='center')

        button_sair = tk.Button(self.root, text="Sair🚩", font=fonts_buttons, bg="gray", fg="black", command=lambda: self.root.destroy())
        button_sair.place(relx=0.5, rely=0.7, relwidth=0.3, relheight=0.1, anchor='center')

    def mostrar_regras(self):
        regras = Regras()
        regras
        self.disable_button_regras()

    def disable_button_regras(self):
        self.button_regras.config(state="disabled")


    def game_initialization(self):
        self.root.destroy()
        interface = Grid()
        interface

    def run(self):
        self.root.mainloop()