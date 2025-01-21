import tkinter as tk
from Core.state_cells import Cell
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas

class Verifica:
    def __init__(self, first_click, mines_positions, free_cells):
        self.first_click =  first_click
        self.mines_positions = mines_positions
        self.free_cells = free_cells
        self.condition_cell = Cell()
        #verifica condição de vitória

    def verificar_condicao(self, first_click, mines_positions, cells_revealed, free_cells):

        print(free_cells)
        print(cells_revealed)
        results_cells_revealed = list(set(cells_revealed))

        if first_click in mines_positions:
            self.defeat()
        elif set(results_cells_revealed) == set(free_cells):
                self.victory()

    def victory(self):
        messagebox.showinfo("Vitoria", "Venceu o jogo!")

    def defeat(self):
        messagebox.showinfo("Derrota", "Perdeu o jogo!")

        