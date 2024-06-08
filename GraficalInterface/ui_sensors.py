import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class SensorUI:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.create_sensor_form()

    def create_sensor_form(self):
        sensor_name_label = ttk.Label(self.frame, text="Nome do Sensor:")
        sensor_name_label.pack(pady=5)
        sensor_name_entry = ttk.Entry(self.frame, width=30)
        sensor_name_entry.pack(pady=5)

        sensor_type_label = ttk.Label(self.frame, text="Tipo do Sensor:")
        sensor_type_label.pack(pady=5)
        sensor_type_entry = ttk.Entry(self.frame, width=30)
        sensor_type_entry.pack(pady=5)

        sensor_location_label = ttk.Label(self.frame, text="Localização do Sensor:")
        sensor_location_label.pack(pady=5)
        sensor_location_entry = ttk.Entry(self.frame, width=30)
        sensor_location_entry.pack(pady=5)

        save_button = ttk.Button(self.frame, text="Salvar", command=self.save_sensor, style="success.TButton")
        save_button.pack(pady=10)

    def save_sensor(self):
        print("Sensor salvo!")

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()