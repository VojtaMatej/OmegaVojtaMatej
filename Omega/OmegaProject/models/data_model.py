import joblib
import pandas as pd


class DataModel:
    def __init__(self):
        self.model_rf = None
        self.encoder = None
        self.scaler = None
        self.model_reg = None
        self.encoder_reg = None
        self.scaler_reg = None

    def load_models(self):
        try:
            self.model_rf = joblib.load("model_rf.bin")
            self.encoder = joblib.load("encoder.bin")
            self.scaler = joblib.load("scaler.bin")
            self.model_reg = joblib.load("model_regression.bin")
            self.encoder_reg = joblib.load("encoder_reg.bin")
            self.scaler_reg = joblib.load("scaler_reg.bin")
            return True
        except Exception as e:
            print(f"Error loading models: {str(e)}")
            return False