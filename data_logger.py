import csv
from datetime import datetime

class DataLogger:
    def __init__(self):
        self.file_name = "traffic_data.csv"
        self.create_file()

    # CREATE CSV FILE
    def create_file(self):
        with open(
            self.file_name,
            mode="w",
            newline=""
        ) as file:
            writer = csv.writer(file)
            writer.writerow([
                "Time",
                "Lane1_Count",
                "Lane2_Count",
                "Divider_Position",
                "Controller_Mode",
                "Alarm_Status",
                "Prediction_Status"
            ])

    # LOG DATA
    def log_data(
        self,
        lane1_count,
        lane2_count,
        divider_position,
        mode,
        alarm,
        prediction
    ):
        current_time = datetime.now().strftime(
            "%H:%M:%S"
        )
        with open(
            self.file_name,
            mode="a",
            newline=""
        ) as file:
            writer = csv.writer(file)

            writer.writerow([
                current_time,
                lane1_count,
                lane2_count,
                divider_position,
                mode,
                alarm,
                prediction
            ])