import tkinter as tk
from tkinter import ttk
import ttkbootstrap as ttk


class ResultView:
    @staticmethod
    def show_analysis_result(parent, location, size, price, predicted_price,
                             price_category, evaluation, style):
        result_window = ttk.Toplevel(parent)
        result_window.title("VÝSLEDEK ANALÝZY")
        result_window.geometry("500x450")

        ttk.Label(result_window, text="VÝSLEDEK ANALÝZY",
                  font=("Helvetica", 16, "bold")).pack(pady=10)

        # Basic info
        info_frame = ttk.Frame(result_window)
        info_frame.pack(pady=5)

        ttk.Label(info_frame, text=f"📍 Lokalita: {location}",
                  font=("Helvetica", 12)).pack(anchor="w")
        ttk.Label(info_frame, text=f"📏 Velikost: {size} m²",
                  font=("Helvetica", 12)).pack(anchor="w")
        ttk.Label(info_frame, text=f"💰 Zadaná cena: {price:,.0f} Kč",
                  font=("Helvetica", 12)).pack(anchor="w")

        # Results
        result_frame = ttk.Frame(result_window)
        result_frame.pack(pady=10)

        ttk.Label(result_frame, text=f"1️⃣ Cenová kategorie: {price_category}",
                  font=("Helvetica", 12)).pack(anchor="w", pady=2)
        ttk.Label(result_frame, text=f"2️⃣ Odhadovaná cena: {predicted_price:,.0f} Kč",
                  font=("Helvetica", 12)).pack(anchor="w", pady=2)
        ttk.Label(result_frame,
                  text=f"3️⃣ Rozdíl: {price - predicted_price:,.0f} Kč ({(price - predicted_price) / predicted_price * 100:+.1f}%)",
                  font=("Helvetica", 12)).pack(anchor="w", pady=2)
        ttk.Label(result_frame, text=f"4️⃣ Hodnocení: {evaluation}",
                  font=("Helvetica", 12), bootstyle=style).pack(anchor="w", pady=5)

        # Close button
        ttk.Button(
            result_window,
            text="ZAVŘÍT",
            command=result_window.destroy,
            bootstyle="danger",
            width=15
        ).pack(pady=10)

    @staticmethod
    def show_prediction_result(parent, location, size, predicted_price):
        result_window = ttk.Toplevel(parent)
        result_window.title("VÝSLEDEK PREDIKCE")
        result_window.geometry("450x350")

        ttk.Label(result_window, text="VÝSLEDEK PREDIKCE",
                  font=("Helvetica", 16, "bold")).pack(pady=10)

        # Basic info
        info_frame = ttk.Frame(result_window)
        info_frame.pack(pady=5)

        ttk.Label(info_frame, text=f"📍 Lokalita: {location}",
                  font=("Helvetica", 12)).pack(anchor="w")
        ttk.Label(info_frame, text=f"📏 Velikost: {size} m²",
                  font=("Helvetica", 12)).pack(anchor="w")

        # Result
        ttk.Label(result_window, text="ODHADOVANÁ CENA:",
                  font=("Helvetica", 12)).pack(pady=5)
        ttk.Label(result_window, text=f"{predicted_price:,.0f} Kč",
                  font=("Helvetica", 14, "bold")).pack(pady=10)

        # Close button
        ttk.Button(
            result_window,
            text="ZAVŘÍT",
            command=result_window.destroy,
            bootstyle="danger",
            width=15
        ).pack(pady=10)