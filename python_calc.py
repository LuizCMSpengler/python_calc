import tkinter as tk
from tkinter import messagebox

# Função que realiza as operações matemáticas
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Erro", "Entrada inválida")

# Função para adicionar o número ou operador ao display da calculadora
def add_to_expression(value):
    entry.insert(tk.END, value)

# Função para limpar o display
def clear():
    entry.delete(0, tk.END)

# Função de limpar entrada (CE)
def clear_entry():
    entry.delete(len(entry.get()) - 1, tk.END)

# Função de porcentagem
def percentage():
    try:
        result = float(entry.get()) / 100
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Erro", "Entrada inválida")

# Função para alternar o sinal ±
def toggle_sign():
    current_text = entry.get()
    if current_text.startswith('-'):
        entry.delete(0)
    else:
        entry.insert(0, '-')

# Configuração da janela principal
root = tk.Tk()
root.title("Calculadora Básica")
root.geometry("300x450")  # Tamanho inicial da janela
root.config(bg="#1E1E1E")

# Campo de entrada para exibir a expressão e resultado
entry = tk.Entry(root, font=('Arial', 20), borderwidth=2, relief="flat", justify="right", bg="#1E1E1E", fg="white", insertbackground="white")
entry.grid(row=0, column=0, columnspan=4, sticky="nsew", pady=10, padx=10, ipady=10)

# Estilo dos botões
button_config = {
    "font": ('Arial', 16),
    "bg": "#333333",
    "fg": "white",
    "activebackground": "#555555",
    "relief": "flat"
}

# Botões da calculadora
buttons = [
    ('%', 1, 0), ('CE', 1, 1), ('C', 1, 2), ('⌫', 1, 3),
    ('1/x', 2, 0), ('x²', 2, 1), ('√', 2, 2), ('/', 2, 3),
    ('7', 3, 0), ('8', 3, 1), ('9', 3, 2), ('*', 3, 3),
    ('4', 4, 0), ('5', 4, 1), ('6', 4, 2), ('-', 4, 3),
    ('1', 5, 0), ('2', 5, 1), ('3', 5, 2), ('+', 5, 3),
    ('±', 6, 0), ('0', 6, 1), (',', 6, 2), ('=', 6, 3)
]

# Função adicional para botões específicos
def backspace():
    current_text = entry.get()
    entry.delete(len(current_text) - 1, tk.END)

def reciprocal():
    try:
        result = 1 / float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Erro", "Entrada inválida")

def square():
    try:
        result = float(entry.get()) ** 2
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Erro", "Entrada inválida")

def square_root():
    try:
        result = float(entry.get()) ** 0.5
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception:
        messagebox.showerror("Erro", "Entrada inválida")

# Configuração do grid para redimensionamento
for i in range(7):  # Define peso para todas as linhas (7 linhas)
    root.grid_rowconfigure(i, weight=1)
for j in range(4):  # Define peso para todas as colunas (4 colunas)
    root.grid_columnconfigure(j, weight=1)

# Adicionando cada botão de número e operador à interface
for (text, row, col) in buttons:
    if text == '=':
        button = tk.Button(root, text=text, **button_config, command=calculate)
        button.config(bg="#A15BFE")  # Definindo cor de fundo do botão "="
    elif text == 'C':
        button = tk.Button(root, text=text, **button_config, command=clear)
    elif text == '⌫':
        button = tk.Button(root, text=text, **button_config, command=backspace)
    elif text == '1/x':
        button = tk.Button(root, text=text, **button_config, command=reciprocal)
    elif text == 'x²':
        button = tk.Button(root, text=text, **button_config, command=square)
    elif text == '√':
        button = tk.Button(root, text=text, **button_config, command=square_root)
    elif text == '%':
        button = tk.Button(root, text=text, **button_config, command=percentage)
    elif text == 'CE':
        button = tk.Button(root, text=text, **button_config, command=clear_entry)
    elif text == '±':
        button = tk.Button(root, text=text, **button_config, command=toggle_sign)
    else:
        button = tk.Button(root, text=text, **button_config, command=lambda t=text: add_to_expression(t))
    button.grid(row=row, column=col, sticky="nsew", padx=3, pady=3)  # Usa sticky="nsew" para expandir

root.mainloop()
