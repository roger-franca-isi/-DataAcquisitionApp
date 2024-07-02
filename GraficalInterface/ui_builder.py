import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb

from GraficalInterface.ui_main import MainUI
from GraficalInterface.ui_mqtt import MqttUI
from GraficalInterface.ui_sensors import SensorUI
from GraficalInterface.ui_showGraph import ShowGraphUI

class ModernApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Aquisição de Dados")
        self.style = tb.Style(theme="cyborg")
        
        # Configuração da grid
        self.root.columnconfigure(0, weight=1)
        self.root.columnconfigure(1, weight=25)
        self.root.rowconfigure(0, weight=1)
        
        # Frame de Navegação
        self.nav_frame = ttk.Frame(root, padding="10")
        self.nav_frame.grid(row=0, column=0, sticky=(tk.N, tk.S, tk.E, tk.W))

        # Frame Principal
        self.main_frame = ttk.Frame(root, padding="10")
        self.main_frame.grid(row=0, column=1, sticky=(tk.N, tk.S, tk.E, tk.W))
        
        # Instâncias das janelas
        self.frames = {
            "MainUI": MainUI(self.main_frame),
            "SensorUI": SensorUI(self.main_frame),
            "MqttUI": MqttUI(self.main_frame),
            "ShowGraphUI": ShowGraphUI(self.main_frame)
            }

        # Botões de Navegação
        self.create_nav_button("Principal", 0, "MainUI")
        self.create_nav_button("Cadastro Sensores", 1, "SensorUI")
        self.create_nav_button("MQTT", 2, "MqttUI")
        self.create_nav_button("Visualização", 3, "ShowGraphUI")
        
        # Conteúdo inicial
        self.show_content("MainUI")

    def create_nav_button(self, text, row, frame_name):
        button = ttk.Button(self.nav_frame, text=text, command=lambda: self.show_content(frame_name))
        button.grid(row=row, column=0, pady=10, sticky=tk.W + tk.E)

    def show_content(self, frame_name):
        # Oculta todos os frames
        for frame in self.frames.values():
            frame.hide()

        # Mostra o frame selecionado
        self.frames[frame_name].show()
