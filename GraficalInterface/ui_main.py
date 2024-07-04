import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class MainUI:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)

        label = ttk.Label(self.frame, text="Sistema de Aquisição de Dados 4.0!", style="primary.TLabel")
        label.pack(expand=True)

        # Frame para os botões
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=20)

        # Botão Iniciar
        self.start_button = ttk.Button(button_frame, text="Iniciar", command=self.start_action, style="success.TButton")
        self.start_button.pack(side=tk.LEFT, padx=10)

        # Botão Parar
        self.stop_button = ttk.Button(button_frame, text="Parar", command=self.stop_action, style="danger.TButton")
        self.stop_button.pack(side=tk.LEFT, padx=10)
       
        self.start_button.state(['!disabled'])
        self.stop_button.state(['disabled'])
        
    def start_action(self):
        self.callback_start();
        self.start_button.state(['disabled'])
        self.stop_button.state(['!disabled'])

    def stop_action(self):
        self.callback_stop();
        self.start_button.state(['!disabled'])
        self.stop_button.state(['disabled'])

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()
            
    def set_callback_start(self, callback):
        self.callback_start = callback
        
    def set_callback_stop(self, callback):
        self.callback_stop = callback
