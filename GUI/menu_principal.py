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
        self.images_definition()
        self.images_moving()
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
        x1, y1, x2, y2 = self.canvas.bbox(self.bomba_imageID1)
        x1b, y1b, x2b, y2b = self.canvas.bbox(self.bandeira_imageID1)

        # Verificar colisões com as bordas
        if x1 <= 0 or x2 >= self.canvas_width:  # Colisão horizontal
            self.dx = -self.dx
        if y1 <= 0 or y2 >= self.canvas_height:  # Colisão vertical
            self.dy = -self.dy

        if x1b <= 0 or x2b >= self.canvas_width:  # Colisão horizontal
            self.dxb = -self.dxb
        if y1b <= 0 or y2b >= self.canvas_height:  # Colisão vertical
            self.dyb = -self.dyb

        

        self.canvas.move(self.bomba_imageID1, self.dx, self.dy)
        self.canvas.move(self.bomba_imageID2, self.dxb, self.dyb)
        self.canvas.move(self.bandeira_imageID1, self.dxb, self.dyb)
        self.canvas.move(self.bandeira_imageID2, self.dxb, self.dyb)
        self.canvas.tag_raise(self.bomba_imageID1)
        self.canvas.tag_raise(self.bandeira_imageID1)
        self.root.after(65, self.images_moving)

    

    def run(self):
        self.root.mainloop()