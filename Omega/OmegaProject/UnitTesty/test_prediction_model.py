import pytest
import pandas as pd
import numpy as np
from models.prediction_model import PredictionModel
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LinearRegression


class TestPredictionModel:
    @pytest.fixture
    def setup_models(self):
        # Setup dummy models and transformers
        locations = ["Praha", "Brno", "Ostrava"]
        encoder = LabelEncoder().fit(locations)
        scaler = StandardScaler().fit([[50], [100], [150]])

        rf_model = RandomForestClassifier()
        X = [[0, 50], [1, 100], [2, 150]]
        y = [1, 2, 3]
        rf_model.fit(X, y)

        reg_model = LinearRegression()
        reg_model.fit(X, [1000000, 2000000, 3000000])

        return rf_model, encoder, scaler, reg_model

    def test_predict_category(self, setup_models):
        rf_model, encoder, scaler, _ = setup_models
        result = PredictionModel.predict_category(rf_model, encoder, scaler, "Brno", 100)
        assert result in [1, 2, 3]

    def test_predict_price(self, setup_models):
        _, encoder, scaler, reg_model = setup_models
        result = PredictionModel.predict_price(reg_model, encoder, scaler, "Brno", 100)
        assert isinstance(result, float)
        assert result > 0

    def test_evaluate_price(self):
        # Test overpriced
        eval1, style1 = PredictionModel.evaluate_price(120, 100)
        assert "PŘEDRAŽENÉ" in eval1
        assert style1 in ["danger", "warning"]

        # Test underpriced
        eval2, style2 = PredictionModel.evaluate_price(80, 100)
        assert "POD TRHEM" in eval2
        assert style2 == "success"

        # Test market price
        eval3, style3 = PredictionModel.evaluate_price(100, 100)
        assert "TRŽNÍ CENA" in eval3
        assert style3 == "success"