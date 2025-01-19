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
        self.mines_positions = None
        self.remaining_times = 5 * 60
        self.setup_window()
        self.create_grid()
        self.create_numbers()
        self.board = [[Cell() for _ in range(self.columns)] for _ in range(self.rows)]
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

        self.timer_label = tk.Label(self.root, text="Tempo 05:00", font=("Arial", 15))
        self.timer_label.place(relx=0.5, rely=0.01, relwidth=0.3, relheight=0.1, anchor='n')

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
        self.canvas.bind("<Button-1>", self.clique)


    def pixel_to_cell(self, pixel_coords):
        x, y = pixel_coords
        offset_x = (self.canvas_width - self.columns * 50) // 2
        offset_y = (self.canvas_height - self.rows * 50) // 2
        cell_y = (y - offset_y) // 50
        cell_x = (x - offset_x) // 50
        return cell_y, cell_x

    def clique(self, event):
        cell = self.pixel_to_cell((event.x, event.y))

        if cell:
            self.first_click = cell
            print(f"First click: {cell}")
            if not self.mines_positions:
                self.generate_mines(cell)
        
        verificar = Verifica(self.first_click, self.mines_positions)
        verificar

    def generate_mines(self, first_click):

        all_positions = [(r, c) for r in range(self.rows) for c in range(self.columns)]

        if first_click in all_positions:
            all_positions.remove(first_click)
        else:
            print(f"Erro: {first_click} não está em all_positions.")
            return

        self.mines_positions = random.sample(all_positions, self.has_mines)
        self.start_time()

        for r, c in self.mines_positions:
            self.board[r][c].is_mine = True
        
        print ("minas COLOCADAS")
        print(self.mines_positions)


    def start_time(self):
        self.update_timer()

    def update_timer(self):
        minutes = self.remaining_times // 60
        seconds = self.remaining_times % 60
        formmated_time = f"Tempo: {minutes:02}:{seconds:02}"

        self.timer_label.config(text=formmated_time)

        if self.remaining_times > 0:
            self.remaining_times -= 1
            self.root.after(1000, self.update_timer)
        else:
            self.timer_label.config(text="Tempo: 00:00")
            self.root.destroy()
            print("Tempo esgotado! O jogo acabou.")


    def calculate_adjacent_mines(self):
        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            ( 0, -1),          ( 0, 1),
            ( 1, -1), ( 1, 0), ( 1, 1)
        ]

        for r in range(self.rows):
            for c in range(self.columns):
                if self.board[r][c].is_mine:
                    continue
                count = 0
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < self.rows and 0 <= nc < self.columns:
                        if self.board[nr][nc].is_mine:
                            count += 1
                self.board[r][c].adjacent_mines = count

        



    def run(self):
        self.root.mainloop()