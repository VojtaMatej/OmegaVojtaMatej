import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


class AnalysisView:
    def __init__(self, parent_frame):
        self.parent_frame = parent_frame
        self.frame = ttk.Frame(self.parent_frame)

        # Title
        ttk.Label(self.frame, text="ANALÝZA NEMOVITOSTI",
                  font=("Helvetica", 16, "bold")).pack(pady=(0, 15))

        # Form
        self.form_frame = ttk.Frame(self.frame)
        self.form_frame.pack()

        # Location
        ttk.Label(self.form_frame, text="LOKALITA:",
                  font=("Helvetica", 12)).grid(row=0, column=0, sticky="w", pady=5, padx=5)
        self.location_combobox = ttk.Combobox(
            self.form_frame,
            width=40,
            font=("Helvetica", 12)
        )
        self.location_combobox.grid(row=0, column=1, pady=5, padx=10)

        # Size
        ttk.Label(self.form_frame, text="VELIKOST (m²):",
                  font=("Helvetica", 12)).grid(row=1, column=0, sticky="w", pady=5, padx=5)
        self.size_entry = ttk.Entry(
            self.form_frame,
            width=15,
            font=("Helvetica", 12)
        )
        self.size_entry.grid(row=1, column=1, sticky="w", pady=5, padx=10)

        # Price
        ttk.Label(self.form_frame, text="CENA (Kč):",
                  font=("Helvetica", 12)).grid(row=2, column=0, sticky="w", pady=5, padx=5)
        self.price_entry = ttk.Entry(
            self.form_frame,
            width=15,
            font=("Helvetica", 12)
        )
        self.price_entry.grid(row=2, column=1, sticky="w", pady=5, padx=10)

        # Analyze button
        self.analyze_btn = ttk.Button(
            self.frame,
            text="SPUSTIT ANALÝZU",
            bootstyle="success",
            width=20
        )
        self.analyze_btn.pack(pady=20)

    def pack(self, **kwargs):
        self.frame.pack(**kwargs)

    def forget(self):
        self.frame.pack_forget()