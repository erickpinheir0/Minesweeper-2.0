import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas

class Revelar:
    def __init__(self):
        #indica o número de bombas ao redor da célula, e verifica se a celula é uma mina
        self.verificar_mina()
        self.revelar_celulas()
