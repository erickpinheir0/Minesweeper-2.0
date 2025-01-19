import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox
from tkinter import Canvas

class Verifica:
    def __init__(self, first_click, mines_positions):
        self.first_click =  first_click
        self.mines_positions = mines_positions
        #verifica condição de vitória
        self.verificar_condicao(self.first_click, self.mines_positions)


    def verificar_condicao(self, first_click, mines_positions):
        print ("first_click", first_click)
        print ("mines_positions", mines_positions)

        if first_click in mines_positions:
            self.defeat()

    def victory(self):

        pass

    def defeat(self):
        messagebox.showinfo("Derrota", "Perdeu o jogo!")

        