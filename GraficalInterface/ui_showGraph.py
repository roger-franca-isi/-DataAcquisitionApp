# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 14:00:24 2024

@author: roger
"""
import tkinter as tk
from tkinter import ttk
import ttkbootstrap as tb
from ttkbootstrap.constants import *

class ShowGraphUI:
    def __init__(self, parent):
        self.frame = ttk.Frame(parent, padding="10")
        self.frame.pack(fill=tk.BOTH, expand=True)
        label = ttk.Label(self.frame, text="Visualização de Gráficos", style="primary.TLabel")
        label.pack(expand=True)

    def show(self):
        self.frame.pack(fill=tk.BOTH, expand=True)

    def hide(self):
        self.frame.pack_forget()