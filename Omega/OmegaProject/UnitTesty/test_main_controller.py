import pytest
from tkinter import Tk
from models.data_model import DataModel
from controllers.main_controller import MainController
from unittest.mock import MagicMock


class TestMainController:
    @pytest.fixture
    def setup(self):
        root = Tk()
        model = DataModel()
        controller = MainController(root, model)
        yield controller, root
        root.destroy()

    def test_switch_mode(self, setup):
        controller, _ = setup
        # Mock sub-controllers
        controller.analysis_controller = MagicMock()
        controller.prediction_controller = MagicMock()

        # Test analysis mode
        controller.mode_var.set(0)
        controller.switch_mode()
        controller.prediction_controller.view.forget.assert_called_once()
        controller.analysis_controller.view.pack.assert_called_once_with(fill='both', expand=True)

        # Test prediction mode
        controller.mode_var.set(1)
        controller.switch_mode()
        controller.analysis_controller.view.forget.assert_called_once()
        controller.prediction_controller.view.pack.assert_called_once_with(fill='both', expand=True)