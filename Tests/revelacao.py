import tkinter as tk
from Core.state_cells import Cell
from Tests.verificar import Verifica
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas

class Revelar:
    def __init__(self, first_click, mines_positions, free_cells, cells_revealed):
        self.first_click = first_click
        self.mines_positions = mines_positions
        self.free_cells = free_cells
        self.cells_revealed = cells_revealed

        self.verificar = Verifica(first_click, mines_positions, free_cells)
        self.condition_cell = Cell()
        #verifica se a celula é uma mina
        self.revelar_celula(first_click)

    def revelar_celula(self, first_click):
         # Verifique se a célula clicada é uma mina
        if first_click in self.mines_positions:
            # Lógica para lidar com a mina (derrota)
            return self.verificar.defeat()
        else:
            # Marcar a célula como revelada
            self.condition_cell.state = "revealed"  # Atualize o estado da célula
            print(f"Célula {first_click} revelada.")
            print(self.cells_revealed)

            # Chame a função para verificar se o jogo foi vencido
            self.verificar.verificar_condicao(first_click, self.mines_positions, self.cells_revealed, self.free_cells)

        pass

    def calcular_adjacent_mines(self):
        pass
