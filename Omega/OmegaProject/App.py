import tkinter as tk
import sys
import io
from models.data_model import DataModel
from controllers.main_controller import MainController

# Nastavení kódování
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.buffer, encoding='utf-8')


def main():
    root = tk.Tk()

    # Inicializace modelu
    model = DataModel()
    if not model.load_models():
        print("Nepodařilo se načíst modely!")
        return

    # Vytvoření hlavního controlleru
    main_controller = MainController(root, model)

    # Spuštění aplikace
    main_controller.run()

    root.mainloop()


if __name__ == "__main__":
    main()