import tkinter as tk
from tkinter import ttk
from tkinter import PhotoImage
from tkinter import messagebox

class Regras(tk.Toplevel):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.exibir_regras()

    def setup_window(self):
        self.title("Regras")
        self.geometry("450x650")
        self.resizable(False, False)
        self.canvas_width = 400
        self.canvas_height = 600
        self.canvas = tk.Canvas(self, width=self.canvas_width, height=self.canvas_height)
        self.canvas.pack()

    def exibir_regras(self):

        label_titulo = tk.Label(self, text="Regras do Jogo", font=("Courier New", 25, "bold"), fg="black")
        label_titulo.place(relx=0.5, rely=0.1, relwidth=0.8, relheight=0.1, anchor='center')

        descricao = """
Objetivo Principal: Descobrir todas as
células do tabuleiro que não contém minas.
Regras:
1. Clique em uma celula 
para revelar o conteúdo dela.

2. Se revelar uma mina, o jogo termina.

3. Se revelar uma celula vazia, 
revela-se o conteudo de todas 
as celulas adjacentes.

4. Se revelar uma bandeira, revela-se o 
conteudo de todas as celulas adjacentes.

5. Se revelar uma bandeira, revela-se 
o conteudo da celula clicada.

6. Se revelar uma celula vazia, 
revela-se o conteudo da celula clicada.

7. Se revelar uma bandeira, 
revela-se o conteudo da celula clicada.

8. Se revelar uma bandeira, 
revela-se o conteudo da celula clicada.

9. Se revelar uma bandeira, 
revela-se o conteudo da celula clicada.

10. Se revelar uma bandeira, 
revela-se o conteudo da celula clicada.
"""

        label_descricao = tk.Label(self, 
        text=descricao,
        justify="center",
        font=("Courier New", 10), 
        fg="black")
        label_descricao.place(relx=0.5, rely=0.15, relwidth=0.9, relheight=0.9, anchor='n')

    def run(self):
        self.mainloop()