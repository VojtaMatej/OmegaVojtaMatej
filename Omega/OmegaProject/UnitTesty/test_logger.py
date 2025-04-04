import pytest
import os
from datetime import datetime
from utils.logger import Logger


class TestLogger:
    def test_log_to_file(self, tmp_path):
        test_file = tmp_path / "test_log.csv"

        # Test creating new file
        Logger.log("Test", "Location", 100, 1000000, 900000, "A", "Good")
        assert os.path.exists("realitni_logs.csv")

        # Test appending to existing file
        initial_size = os.path.getsize("realitni_logs.csv")
        Logger.log("Test2", "Location2", 200, 2000000, 1800000, "B", "Excellent")
        assert os.path.getsize("realitni_logs.csv") > initial_size

        # Cleanup
        os.remove("realitni_logs.csv")