import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class MqttUI:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding="10")
        self.create_mqtt_form()

    def create_mqtt_form(self):
        self.mqtt_name_label = ttk.Label(self.frame, text="Nome do Broker")
        self.mqtt_name_label.pack(pady=5)
        self.mqtt_name_entry = ttk.Entry(self.frame, width=30)
        self.mqtt_name_entry.pack(pady=5)

        self.mqtt_ip_label = ttk.Label(self.frame, text="IP do Broker")
        self.mqtt_ip_label.pack(pady=5)
        self.mqtt_ip_entry = ttk.Entry(self.frame, width=30)
        self.mqtt_ip_entry.pack(pady=5)

        self.mqtt_port_label = ttk.Label(self.frame, text="Porta do Broker")
        self.mqtt_port_label.pack(pady=5)
        self.mqtt_port_entry = ttk.Entry(self.frame, width=30)
        self.mqtt_port_entry.pack(pady=5)
        
        self.mqtt_save_broker_button = ttk.Button(self.frame, text="Salvar", command=self.save_broker, style="success.TButton")
        self.mqtt_save_broker_button.pack(pady=10)
        
        # Frame para os botões de conectar e desconectar
        button_frame = ttk.Frame(self.frame)
        button_frame.pack(pady=10)
        
        self.mqtt_disconnect_broker_button = ttk.Button(button_frame, text="Desconectar", command=self.disconnect_broker, style="success.TButton")
        self.mqtt_disconnect_broker_button.grid(row=0, column=0, padx=5)
        self.mqtt_disconnect_broker_button.state(['disabled'])

        self.mqtt_connect_broker_button = ttk.Button(button_frame, text="Conectar", command=self.connect_broker, style="success.TButton")
        self.mqtt_connect_broker_button.grid(row=0, column=1, padx=5)
        self.mqtt_connect_broker_button.state(['disabled'])

    def save_broker(self):
        print("ui_mqtt - Salvar informacoes no banco de dados!")
        mqtt_name = self.mqtt_name_entry.get()
        mqtt_ip = self.mqtt_ip_entry.get()
        mqtt_port = self.mqtt_port_entry.get()
  
        self.save_callback(mqtt_name, mqtt_ip, mqtt_port)
        
        self.mqtt_connect_broker_button.state(['!disabled'])
            
    def connect_broker(self):
        print("Disparar comando de conectar com o broker")
        mqtt_ip = self.mqtt_ip_entry.get()
        mqtt_port = self.mqtt_port_entry.get()
        self.connect_callback(mqtt_ip, mqtt_port);
        
        self.mqtt_name_entry.configure(state='readonly')
        self.mqtt_ip_entry.configure(state='readonly')
        self.mqtt_port_entry.configure(state='readonly')
        self.mqtt_save_broker_button.state(['disabled'])
        self.mqtt_disconnect_broker_button.state(['!disabled'])
        self.mqtt_connect_broker_button.state(['disabled'])

    def disconnect_broker(self):
        print("Disparar comando de desconectar com o broker")
        self.disconnect_callback()
        self.mqtt_name_entry.configure(state='normal')
        self.mqtt_ip_entry.configure(state='normal')
        self.mqtt_port_entry.configure(state='normal')
        self.mqtt_save_broker_button.state(['!disabled'])
        self.mqtt_disconnect_broker_button.state(['disabled'])
        self.mqtt_connect_broker_button.state(['!disabled'])
        
    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()
    
    def set_callback_save_button(self, callback):
        self.save_callback = callback
        
    def set_callback_connect_button(self, callback):
        self.connect_callback = callback

    def set_callback_disconnect_button(self, callback):
        self.disconnect_callback = callback
            
    def insert_form_data(self, broker_name, broker_ip, broker_port):
        if broker_name is not None:        
            self.mqtt_name_entry.delete(0, tk.END)
            self.mqtt_name_entry.insert(0, broker_name)
            
            self.mqtt_ip_entry.delete(0, tk.END)
            self.mqtt_ip_entry.insert(0, broker_ip)
            
            self.mqtt_port_entry.delete(0, tk.END)
            self.mqtt_port_entry.insert(0, broker_port)
        
            self.mqtt_connect_broker_button.state(['!disabled'])
