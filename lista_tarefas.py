import tkinter as tk
from tkinter import messagebox

def adicionar_tarefa():
    tarefa = entrada_tarefa.get()
    if tarefa:
        lista_tarefas.insert(tk.END, tarefa)
        entrada_tarefa.delete(0, tk.END)
    else:
        messagebox.showwarning("Aviso", "Por favor, digite uma tarefa!")

def remover_tarefa():
    try:
        selecionado = lista_tarefas.curselection()[0]
        lista_tarefas.delete(selecionado)
    except IndexError:
        messagebox.showwarning("Aviso", "Selecione uma tarefa para remover!")

janela = tk.Tk()
janela.title("Lista de Tarefas")

entrada_tarefa = tk.Entry(janela, width=40)
entrada_tarefa.pack(pady=10)

botao_adicionar = tk.Button(janela, text="Adicionar Tarefa", command=adicionar_tarefa)
botao_remover = tk.Button(janela, text="Remover Tarefa", command=remover_tarefa)
botao_adicionar.pack()
botao_remover.pack()

lista_tarefas = tk.Listbox(janela, width=50)
lista_tarefas.pack()

janela.mainloop()
