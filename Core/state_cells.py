import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas
import random

class Cell:
    def __init__(self):
        #lógica de definição de minas no tabuleiro de forma aleatória
        self.is_mine = False
        self.adjacent_mines = 0
        self.state = "hidden"
        

