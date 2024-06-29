import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class SensorUI:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        self.create_sensor_form()
        self.create_sensor_list()

    def create_sensor_form(self):
        self.sensor_tag_label = ttk.Label(self.frame, text="Tag do Sensor:")
        self.sensor_tag_label.pack(pady=5)
        self.sensor_tag_entry = ttk.Entry(self.frame, width=30)
        self.sensor_tag_entry.pack(pady=5)

        self.sensor_implementation_label = ttk.Label(self.frame, text="Implementação:")
        self.sensor_implementation_label.pack(pady=5)
        self.sensor_implementation_entry = ttk.Entry(self.frame, width=30)
        self.sensor_implementation_entry.pack(pady=5)

        self.sensor_data1_label = ttk.Label(self.frame, text="Dado Coletado:")
        self.sensor_data1_label.pack(pady=5)
        self.sensor_data1_entry = ttk.Entry(self.frame, width=30)
        self.sensor_data1_entry.pack(pady=5)
        
        self.sensor_unit1_label = ttk.Label(self.frame, text="Unidade de Medida:")
        self.sensor_unit1_label.pack(pady=5)
        self.sensor_unit1_options = ["C", "Bar", "N", "V", "RPM"]
        self.sensor_unit1_combobox = ttk.Combobox(self.frame, values=self.sensor_unit1_options, state="readonly")
        self.sensor_unit1_combobox.pack(pady=5)

        # Frame for buttons
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=10)

        self.save_button = ttk.Button(button_frame, text="Salvar", command=self.save_sensor, style="success.TButton")
        self.save_button.pack(side=tk.LEFT, padx=5)

        self.delete_button = ttk.Button(button_frame, text="Excluir", command=self.delete_sensor, style="danger.TButton")
        self.delete_button.pack(side=tk.LEFT, padx=5)

    def create_sensor_list(self):
        self.list_frame = ttk.Frame(self.frame)
        self.list_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True)

        self.sensor_listbox = tk.Listbox(self.list_frame, width=40)
        self.sensor_listbox.pack(fill=tk.BOTH, expand=True, pady=10)

    def save_sensor(self):
        sensor_tag = self.sensor_tag_entry.get()
        sensor_implement = self.sensor_implementation_entry.get()
        sensor_data1 = self.sensor_data1_entry.get()
        sensor_unit1 = self.sensor_unit1_combobox.get()

        self.save_callback(sensor_tag, sensor_implement, sensor_data1, sensor_unit1);
        self.sensor_listbox.insert(tk.END, str(sensor_tag))

    def delete_sensor(self):     
        selected = self.sensor_listbox.curselection()
        
        if selected:
            sensor_tag = self.sensor_listbox.get(selected)
            self.delete_callback(str(sensor_tag))
            self.sensor_listbox.delete(selected)
            print(f'Sensor excluído = {sensor_tag}')

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()
        
    def insert_sensor_list(self, sensor_tag):
        self.sensor_listbox.insert(tk.END, str(sensor_tag))
    
    def set_callback_save_button(self, callback):
        self.save_callback = callback
        
    def set_callback_delete_button(self, callback):
        self.delete_callback = callback