from datetime import datetime
import os


class Logger:
    @staticmethod
    def log(action, location, size=None, price=None, predicted_price=None,
            price_category=None, evaluation=None):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_entry = (f"{timestamp},{action},{location},{size},{price},"
                     f"{predicted_price},{price_category},{evaluation}\n")

        if not os.path.exists("realitni_logs.csv"):
            with open("realitni_logs.csv", "w", encoding="utf-8") as f:
                f.write("timestamp,action,location,size_m2,input_price,"
                        "predicted_price,price_category,evaluation\n")

        with open("realitni_logs.csv", "a", encoding="utf-8") as f:
            f.write(log_entry)