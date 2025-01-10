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
            self.bomba_imageID = self.canvas.create_image(5, 5, image=self.bomba_image, anchor=tk.NW)

            self.dx = 10
            self.dy = 10
        except:
            print("Error loading image")

        self.images_moving()

    def images_moving(self):
        x1, y1, x2, y2 = self.canvas.bbox(self.bomba_imageID)

        # Verificar colisões com as bordas
        if x1 <= 0 or x2 >= self.canvas_width:  # Colisão horizontal
            self.dx = -self.dx
        if y1 <= 0 or y2 >= self.canvas_height:  # Colisão vertical
            self.dy = -self.dy

        self.canvas.move(self.bomba_imageID, self.dx, self.dy)
        self.canvas.tag_raise(self.bomba_imageID)
        self.root.after(65, self.images_moving)



    def run(self):
        self.root.mainloop()