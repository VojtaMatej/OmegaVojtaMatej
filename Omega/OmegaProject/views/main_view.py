import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


class MainView:
    def __init__(self, root):
        self.root = root
        self.style = ttk.Style(theme="minty")
        self.create_widgets()

    def create_widgets(self):
        # Frame pro výběr režimu
        self.mode_frame = ttk.Frame(self.root)

        # Hlavní obsahový frame
        self.main_frame = ttk.Frame(self.root)

        # Tlačítko pro zavření
        self.close_btn = ttk.Button(
            self.root,
            text="ZAVŘÍT APLIKACI",
            bootstyle="danger",
            width=25
        )

    def pack_all(self):
        self.mode_frame.pack(fill=tk.X, padx=10, pady=10)
        self.main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        self.close_btn.pack(side=tk.BOTTOM, pady=15, padx=20)

    def setup_mode_selection(self, mode_var, command):
        ttk.Label(self.mode_frame, text="VYBERTE REŽIM:",
                  font=("Helvetica", 12, "bold")).pack(side=tk.LEFT)

        ttk.Radiobutton(
            self.mode_frame,
            text="ANALÝZA NEMOVITOSTI",
            variable=mode_var,
            value=0,
            command=command,
            bootstyle="info-toolbutton"
        ).pack(side=tk.LEFT, padx=15)

        ttk.Radiobutton(
            self.mode_frame,
            text="PREDIKCE CENY",
            variable=mode_var,
            value=1,
            command=command,
            bootstyle="info-toolbutton"
        ).pack(side=tk.LEFT)