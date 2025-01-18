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
        label_titulo.place(relx=0.5, rely=0.085, relwidth=0.8, relheight=0.1, anchor='center')

        descricao = """
Objetivo Principal: Revelar todas as
células do tabuleiro que não contém minas.

Como Jogar:
1. Clique com o botão esquerdo em uma célula 
para revelar o conteúdo dela.

2. Se a célula que foi revelada contém uma mina, 
o jogo termina e o jogador perde.

3. Se o jogador revelar uma celula vazia, 
revela-se o conteudo de todas as 
celulas adjacentes, caso nenhuma contenha minas.

4. O jogador pode marcar celulas que acredita 
conterem minas com uma bandeira, 
ao usar o botão direito.

5. O número indicado em cima das celulas reveladas 
indica o número de minas nas celulas adjacentes.

6. O jogo tem um tempo limite de 1 minuto, 
podendo ser aumentado no grau de dificuldade.

7. Vencer o Jogo: Para vencer o jogo, o jogador 
deve revelar todas as celulas que não 
contém minas dentro do tempo limite.

8. Derrota: O jogo termina quando o jogador revela 
uma celula contendo uma mina, 
ou quando o tempo limite expirar.

"""

        label_descricao = tk.Label(self, 
        text=descricao,
        justify="center",
        font=("Courier New", 10), 
        fg="black")
        label_descricao.place(relx=0.5, rely=0.15, relwidth=0.9, relheight=0.8, anchor='n')

    def run(self):
        self.mainloop()