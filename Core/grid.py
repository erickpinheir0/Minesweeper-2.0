import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas

class Cell:
    def __init__(self, x, y):
        #lógica de definição de minas no tabuleiro de forma aleatória
        self.x = x
        self.y = y
        self.is_mine = False
        self.state = "hidden"
