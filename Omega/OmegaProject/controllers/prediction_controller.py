from tkinter import messagebox
from utils.logger import Logger
from models.prediction_model import PredictionModel


class PredictionController:
    def __init__(self, parent_frame, model):
        self.parent_frame = parent_frame
        self.model = model
        self.view = None

    def initialize(self):
        from views.prediction_view import PredictionView
        self.view = PredictionView(self.parent_frame)

        # Set up event bindings
        self.view.location_combobox.bind("<KeyRelease>", self.update_suggestions)
        self.view.predict_btn.config(command=self.predict_price)

        # Initialize combobox values
        if self.model.encoder_reg is not None:
            self.view.location_combobox['values'] = list(self.model.encoder_reg.classes_)[:20]

    def update_suggestions(self, event=None):
        if self.model.encoder_reg is None:
            return
        typed = self.view.location_combobox.get().lower()
        suggestions = [loc for loc in self.model.encoder_reg.classes_ if typed in loc.lower()]
        self.view.location_combobox['values'] = suggestions[:20]

    def find_best_location_match(self, user_input):
        if not user_input or self.model.encoder_reg is None:
            return None

        user_input = user_input.lower().strip()
        available_locations = self.model.encoder_reg.classes_

        for loc in available_locations:
            if user_input == loc.lower():
                return loc

        for loc in available_locations:
            if user_input in loc.lower():
                return loc

        return None

    def predict_price(self):
        try:
            location_input = self.view.location_combobox.get().strip()
            size = self.view.size_entry.get().strip()

            if not all([location_input, size]):
                messagebox.showerror("CHYBA!", "VYPLŇTE VŠECHNY ÚDAJE!")
                return

            try:
                size_m2 = float(size)
            except ValueError:
                messagebox.showerror("CHYBA!", "VELIKOST MUSÍ BÝT ČÍSLO!")
                return

            if size_m2 <= 0:
                messagebox.showerror("CHYBA!", "VELIKOST MUSÍ BÝT VĚTŠÍ NEŽ 0!")
                return

            # Find location
            location = self.find_best_location_match(location_input)
            if location is None:
                messagebox.showerror("CHYBA!", f"LOKALITA '{location_input}' NEBYLA NALEZENA!")
                return

            # Predict price
            predicted_price = PredictionModel.predict_price(
                self.model.model_reg,
                self.model.encoder_reg,
                self.model.scaler_reg,
                location,
                size_m2
            )

            # Show results
            from views.result_view import ResultView
            ResultView.show_prediction_result(
                self.parent_frame,
                location,
                size_m2,
                predicted_price
            )

            # Log
            Logger.log(
                action="Predikce ceny",
                location=location,
                size=size_m2,
                predicted_price=predicted_price
            )

        except Exception as e:
            messagebox.showerror("CHYBA!", f"NASTALA CHYBA:\n{str(e)}")