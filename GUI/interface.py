import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

class Grid:
    def __init__(self, row, column, num_mines):
        self.row = row
        self.column = column
        self.num_mines = num_mines

