from tkinter import messagebox
from utils.logger import Logger
from models.prediction_model import PredictionModel
from views.result_view import ResultView


class AnalysisController:
    def __init__(self, parent_frame, model):
        self.parent_frame = parent_frame
        self.model = model
        self.view = None

    def initialize(self):
        from views.analysis_view import AnalysisView
        self.view = AnalysisView(self.parent_frame)

        # Set up event bindings
        self.view.location_combobox.bind("<KeyRelease>", self.update_suggestions)
        self.view.analyze_btn.config(command=self.analyze)

        # Initialize combobox values
        if self.model.encoder is not None:
            self.view.location_combobox['values'] = list(self.model.encoder.classes_)[:20]

    def update_suggestions(self, event=None):
        if self.model.encoder is None:
            return
        typed = self.view.location_combobox.get().lower()
        suggestions = [loc for loc in self.model.encoder.classes_ if typed in loc.lower()]
        self.view.location_combobox['values'] = suggestions[:20]

    def find_best_location_match(self, user_input):
        if not user_input or self.model.encoder is None:
            return None

        user_input = user_input.lower().strip()
        available_locations = self.model.encoder.classes_

        for loc in available_locations:
            if user_input == loc.lower():
                return loc

        for loc in available_locations:
            if user_input in loc.lower():
                return loc

        return None

    def analyze(self):
        try:
            location_input = self.view.location_combobox.get().strip()
            size = self.view.size_entry.get().strip()
            price = self.view.price_entry.get().strip()

            if not all([location_input, size, price]):
                messagebox.showerror("CHYBA!", "VYPLŇTE VŠECHNY ÚDAJE!")
                return

            try:
                size_m2 = float(size)
                price_value = float(price)
            except ValueError:
                messagebox.showerror("CHYBA!", "VELIKOST A CENA MUSÍ BÝT ČÍSLA!")
                return

            if size_m2 <= 0 or price_value <= 0:
                messagebox.showerror("CHYBA!", "HODNOTY MUSÍ BÝT VĚTŠÍ NEŽ 0!")
                return

            # 1. Predict price category
            location = self.find_best_location_match(location_input)
            if location is None:
                messagebox.showerror("CHYBA!", f"LOKALITA '{location_input}' NEBYLA NALEZENA!")
                return

            price_category = PredictionModel.predict_category(
                self.model.model_rf,
                self.model.encoder,
                self.model.scaler,
                location,
                size_m2
            )

            # 2. Predict price
            predicted_price = PredictionModel.predict_price(
                self.model.model_reg,
                self.model.encoder_reg,
                self.model.scaler_reg,
                location,
                size_m2
            )

            # 3. Evaluate
            evaluation, style = PredictionModel.evaluate_price(price_value, predicted_price)

            # Show results
            ResultView.show_analysis_result(
                self.parent_frame,
                location,
                size_m2,
                price_value,
                predicted_price,
                price_category,
                evaluation,
                style
            )

            # Log
            Logger.log(
                action="Analýza",
                location=location,
                size=size_m2,
                price=price_value,
                predicted_price=predicted_price,
                price_category=price_category,
                evaluation=evaluation
            )

        except Exception as e:
            messagebox.showerror("CHYBA!", f"NASTALA CHYBA:\n{str(e)}")