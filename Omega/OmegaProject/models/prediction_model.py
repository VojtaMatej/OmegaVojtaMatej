import pandas as pd


class PredictionModel:
    @staticmethod
    def predict_category(model, encoder, scaler, location, size):
        location_encoded = encoder.transform([location])[0]
        input_data = pd.DataFrame([[location_encoded, size]],
                                  columns=["location", "size_m2"])
        scaled_input = scaler.transform(input_data)
        return model.predict(scaled_input)[0]

    @staticmethod
    def predict_price(model, encoder, scaler, location, size):
        location_encoded = encoder.transform([location])[0]
        size_normalized = scaler.transform([[size]])[0][0]
        input_data = pd.DataFrame([[location_encoded, size_normalized]],
                                  columns=["location", "size_m2"])
        return model.predict(input_data)[0]

    @staticmethod
    def evaluate_price(input_price, predicted_price):
        difference = input_price - predicted_price
        difference_percent = (difference / predicted_price) * 100

        if difference_percent > 20:
            return "VÝRAZNĚ PŘEDRAŽENÉ ❌", "danger"
        elif difference_percent > 10:
            return "MÍRNĚ PŘEDRAŽENÉ ⚠️", "warning"
        elif difference_percent < -20:
            return "VÝRAZNĚ POD TRHEM 💰", "success"
        elif difference_percent < -10:
            return "MÍRNĚ POD TRHEM 👍", "success"
        else:
            return "TRŽNÍ CENA ✅", "success"