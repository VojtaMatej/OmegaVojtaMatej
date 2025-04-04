import tkinter as tk
from controllers.analysis_controller import AnalysisController
from controllers.prediction_controller import PredictionController
from views.main_view import MainView


class MainController:
    def __init__(self, root, model):
        self.root = root
        self.model = model
        self.view = MainView(root)
        self.mode_var = tk.IntVar(value=0)

        # Inicializace podřízených controllerů
        self.analysis_controller = AnalysisController(self.view.main_frame, model)
        self.prediction_controller = PredictionController(self.view.main_frame, model)

        # Nastavení ovládacích prvků
        self.setup_controls()

    def setup_controls(self):
        # Režimy
        self.view.setup_mode_selection(self.mode_var, self.switch_mode)
        self.view.close_btn.config(command=self.root.destroy)

        # Inicializace views
        self.analysis_controller.initialize()
        self.prediction_controller.initialize()

        # Výchozí režim
        self.switch_mode()

    def run(self):
        self.view.pack_all()

    def switch_mode(self):
        if self.mode_var.get() == 0:  # Analýza
            self.prediction_controller.view.forget()
            self.analysis_controller.view.pack(fill=tk.BOTH, expand=True)
        else:  # Predikce
            self.analysis_controller.view.forget()
            self.prediction_controller.view.pack(fill=tk.BOTH, expand=True)