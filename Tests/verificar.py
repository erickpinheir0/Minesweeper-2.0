import tkinter as tk
from Core.state_cells import Cell
from Tests.revelacao import Revelar
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas

class Verifica:
    def __init__(self, first_click, mines_positions):
        self.first_click =  first_click
        self.mines_positions = mines_positions
        self.condition_cell = Cell()
        #verifica condição de vitória
        self.verificar_condicao(self.first_click, self.mines_positions)


    def verificar_condicao(self, first_click, mines_positions):

        if first_click in mines_positions:
            self.defeat()
        elif first_click not in mines_positions:
            self.condition_cell.state_cells = "revealed"
            revelar = Revelar()
            revelar.revelar_celula(first_click)


    def victory(self):

        pass

    def defeat(self):
        messagebox.showinfo("Derrota", "Perdeu o jogo!")

        