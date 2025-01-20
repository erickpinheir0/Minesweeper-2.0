import tkinter as tk
from GUI.interface import Grid
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas

class Revelar:
    def __init__(self):
        #verifica se a celula é uma mina
        self.revelar_celula()
        #indica o número de bombas ao redor da célula, e verifica se a celula é uma mina
        self.calcular_adjacent_mines()

    def revelar_celula(self, first_click):
        

        pass

    def calcular_adjacent_mines(self):
        pass
