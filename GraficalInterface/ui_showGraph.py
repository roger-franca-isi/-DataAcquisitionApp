import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

class ShowGraphUI:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        # Configuração do layout da frame principal
        self.frame.columnconfigure(0, weight=1)
        self.frame.columnconfigure(1, weight=10)
        self.frame.rowconfigure(0, weight=1)

        # Adicionando a lista à esquerda
        self.create_listbox()

        # Adicionando o espaço para gráficos à direita
        self.create_plot_area()

    def create_listbox(self):
        # Frame para a lista
        list_frame = ttk.Frame(self.frame)
        list_frame.grid(row=0, column=0, sticky="nswe")

        # Scrollbar para a lista
        scrollbar = ttk.Scrollbar(list_frame, orient=tk.VERTICAL)
        self.listbox = tk.Listbox(list_frame, yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.listbox.yview)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

        # Bind do evento de clique duplo
        self.listbox.bind("<Double-Button-1>", self.on_double_click)
        
    def create_plot_area(self):
        # Frame para o gráfico
        plot_frame = ttk.Frame(self.frame)
        plot_frame.grid(row=0, column=1, sticky="nswe")

        # Criando uma figura do Matplotlib
        self.fig = Figure(figsize=(5, 4), dpi=100)
        self.ax = self.fig.add_subplot(111)

        # Canvas do Tkinter para renderizar o gráfico
        self.canvas = FigureCanvasTkAgg(self.fig, master=plot_frame)
        self.canvas.draw()
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=True)

        # Exemplo de gráfico
        self.plot_example_graph()

    def on_double_click(self, event):
        # Obtém o índice do item clicado duas vezes
        selection = self.listbox.curselection()
        
        if selection:
            index = selection[0]
            value = self.listbox.get(index)
            print(f"Item duplo clicado: {value}")
            # Aqui você pode adicionar a lógica que deseja executar ao clicar duas vezes no item
            self.plot_example_graph()
            
    def plot_example_graph(self):
        # Dados de exemplo
        x = [1, 2, 3, 4, 5]
        y = [1, 4, 2, 5, 3]

        # Plotando no gráfico
        self.ax.plot(x, y)
        self.canvas.draw()

    def insert_sensor(self, sensor_tag):
        self.listbox.insert(tk.END, sensor_tag)

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()
        