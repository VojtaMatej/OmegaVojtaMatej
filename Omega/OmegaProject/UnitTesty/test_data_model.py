import pytest
from models.data_model import DataModel
import joblib
import os


class TestDataModel:
    @pytest.fixture
    def model(self):
        return DataModel()

    def test_load_models_success(self, model, tmp_path):
        # Create dummy model files
        dummy_model = {"dummy": "model"}
        for file in ["model_rf.bin", "encoder.bin", "scaler.bin",
                     "model_regression.bin", "encoder_reg.bin", "scaler_reg.bin"]:
            joblib.dump(dummy_model, tmp_path / file)

        original_dir = os.getcwd()
        try:
            os.chdir(tmp_path)
            assert model.load_models() is True
            assert model.model_rf is not None
            assert model.encoder is not None
            assert model.scaler is not None
            assert model.model_reg is not None
            assert model.encoder_reg is not None
            assert model.scaler_reg is not None
        finally:
            os.chdir(original_dir)

    def test_load_models_failure(self, model):
        assert model.load_models() is False