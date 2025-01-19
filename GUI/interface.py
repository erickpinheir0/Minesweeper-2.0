from re import X
import tkinter as tk
import random
from Core.state_cells import Cell
from Tests.revelacao import Revelar
from Tests.verificar import Verifica
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

class Grid:
    def __init__(self, rows, columns, has_mines):
        self.rows = rows
        self.columns = columns
        self.has_mines = has_mines
        self.setup_window()
        self.create_grid()
        self.create_numbers()
        self.board = [[Cell() for _ in range(self.columns)] for _ in range(self.rows)]
        self.mines_position = [ ]
        self.run()

    def setup_window(self):
        self.root = tk.Tk()
        self.root.title("Minesweeper")
        self.root.geometry("550x800")
        self.root.resizable(False, False)
        self.canvas_width = 550
        self.canvas_height = 800
        self.canvas = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def create_grid(self):

        #Calcula o tamanho total do tabuleiro, com base nas linhas e colunas
        total_width = self.columns * 50
        total_height = self.rows * 50

        #Calcula o offset para centralizar o tabuleiro, pega a diferença entre o tamanho do canvas e o tabuleiro, divide por 2
        offset_x = (self.canvas_width - total_width) // 2
        offset_y = (self.canvas_height - total_height) // 2

        self.lista_linhas = []
        self.lista_colunas = []

        #Cria o tabuleiro, com base nas linhas e colunas, e no espaçamento calculado
        for i in range(self.rows):
            for j in range(self.columns):
                self.canvas.create_rectangle(
                    offset_x + i * 50, 
                    offset_y + j * 50, 
                    offset_x + (i + 1) * 50, 
                    offset_y + (j + 1) * 50, 
                    fill="darkred", 
                    outline="black", 
                    width=2, 
                    tags=f"cell_{i}_{j}")
                self.r = i
                self.c = j
                self.lista_linhas.append(self.r)
                self.lista_colunas.append(self.c)
        


    def create_numbers(self):
        for j in range(self.columns):
            self.canvas.create_text(
                72 + j * 50,
                150,
                text=str(j),
                fill="black",
                font=("Arial", 15)
            )

        for i in range(self.rows):
            self.canvas.create_text(
                20,
                200 + i * 50,
                text=str(i),
                fill="black",
                font=("Arial", 15)
            )
        clique = self.canvas.bind("<Button-1>", self.clique)
        

    def clique(self, event):
        linha = event.y 
        coluna = event.x 
        first_click = (linha, coluna)

        self.generate_mines(first_click)

    def generate_mines(self, first_click):
        all_positions = [(r, c) for r in range(self.lista_linhas) for c in range(self.lista_colunas)]
        all_positions.remove(first_click)

        self.mines_positions = random.sample(all_positions, self.has_mines)

        for r, c in self.mines_positions:
            self.board[r][c].is_mine = True
        
        print ("minas COLOCADAS")


    def run(self):
        self.root.mainloop()