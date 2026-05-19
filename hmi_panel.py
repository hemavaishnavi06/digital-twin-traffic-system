from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QPushButton
)

from PyQt5.QtCore import Qt

from config import *


class HMIPanel:

    def __init__(self, parent):

        self.parent = parent

        # PANEL

        self.panel = QWidget(parent)

        self.panel.setStyleSheet(f"""
            background-color: rgb{PANEL_BACKGROUND};
            border-right: 3px solid cyan;
        """)

        # STYLES

        self.label_style = f"""
            color: white;
            font-size: {LABEL_FONT_SIZE}px;
            font-weight: bold;
        """

        self.button_style = f"""
            background-color: #333333;
            color: white;
            font-size: {BUTTON_FONT_SIZE}px;
            font-weight: bold;
            border: 2px solid cyan;
        """

        # TITLE

        self.title_label = QLabel(
            "HMI CONTROL PANEL",
            self.panel
        )

        self.title_label.setStyleSheet(f"""
            color: cyan;
            font-size: {TITLE_FONT_SIZE}px;
            font-weight: bold;
        """)

        # LABELS

        self.lane1_label = QLabel(self.panel)
        self.lane1_label.setStyleSheet(
            self.label_style
        )

        self.lane2_label = QLabel(self.panel)
        self.lane2_label.setStyleSheet(
            self.label_style
        )

        self.divider_label = QLabel(self.panel)
        self.divider_label.setStyleSheet(
            self.label_style
        )

        self.mode_label = QLabel(self.panel)
        self.mode_label.setStyleSheet(
            self.label_style
        )

        self.alarm_label = QLabel(self.panel)
        self.alarm_label.setStyleSheet(
            self.label_style
        )

        self.sensor1_label = QLabel(self.panel)
        self.sensor1_label.setStyleSheet(
            self.label_style
        )

        self.sensor2_label = QLabel(self.panel)
        self.sensor2_label.setStyleSheet(
            self.label_style
        )

        self.prediction_label = QLabel(
            self.panel
        )

        self.prediction_label.setStyleSheet(f"""
            color: cyan;
            font-size: 13px;
            font-weight: bold;
        """)

        # LOG TITLE

        self.log_title = QLabel(
            "SYSTEM LOGS",
            self.panel
        )

        self.log_title.setStyleSheet("""
            color: cyan;
            font-size: 16px;
            font-weight: bold;
        """)

        # LOG BOX

        self.log_label = QLabel(self.panel)

        self.log_label.setStyleSheet(f"""
            color: white;
            font-size: {LOG_FONT_SIZE}px;
            background-color: black;
            border: 2px solid cyan;
            padding: 4px;
        """)

        self.log_label.setAlignment(
            Qt.AlignTop
        )

        # BUTTONS

        self.auto_button = QPushButton(
            "AUTO",
            self.panel
        )

        self.manual_button = QPushButton(
            "MANUAL",
            self.panel
        )

        self.emergency_button = QPushButton(
            "EMERGENCY",
            self.panel
        )

        self.motor_fault_button = QPushButton(
            "MOTOR",
            self.panel
        )

        self.sensor_fault_button = QPushButton(
            "SENSOR",
            self.panel
        )

        self.comm_fault_button = QPushButton(
            "COMM",
            self.panel
        )

        self.reset_fault_button = QPushButton(
            "RESET",
            self.panel
        )

        self.emergency_vehicle_button = QPushButton(
            "AMBULANCE",
            self.panel
        )

        # APPLY BUTTON STYLES

        buttons = [

            self.auto_button,
            self.manual_button,
            self.emergency_button,
            self.motor_fault_button,
            self.sensor_fault_button,
            self.comm_fault_button,
            self.reset_fault_button,
            self.emergency_vehicle_button
        ]

        for button in buttons:

            button.setStyleSheet(
                self.button_style
            )

    # PANEL GEOMETRY

    def update_geometry(self, height):

        self.panel.setGeometry(
            0,
            0,
            PANEL_WIDTH,
            height
        )

        self.title_label.setGeometry(
            20,
            10,
            250,
            25
        )

        y = 45

        step = 28

        self.lane1_label.setGeometry(
            20,
            y,
            260,
            22
        )

        self.lane2_label.setGeometry(
            20,
            y + step,
            260,
            22
        )

        self.divider_label.setGeometry(
            20,
            y + step * 2,
            260,
            22
        )

        self.mode_label.setGeometry(
            20,
            y + step * 3,
            260,
            22
        )

        self.alarm_label.setGeometry(
            20,
            y + step * 4,
            260,
            22
        )

        self.sensor1_label.setGeometry(
            20,
            y + step * 5,
            260,
            22
        )

        self.sensor2_label.setGeometry(
            20,
            y + step * 6,
            260,
            22
        )

        self.prediction_label.setGeometry(
            20,
            y + step * 7,
            260,
            35
        )

        # BUTTONS

        button_y = 300

        self.auto_button.setGeometry(
            20,
            button_y,
            120,
            32
        )

        self.manual_button.setGeometry(
            150,
            button_y,
            120,
            32
        )

        self.emergency_button.setGeometry(
            20,
            button_y + 40,
            250,
            32
        )

        self.motor_fault_button.setGeometry(
            20,
            button_y + 85,
            120,
            32
        )

        self.sensor_fault_button.setGeometry(
            150,
            button_y + 85,
            120,
            32
        )

        self.comm_fault_button.setGeometry(
            20,
            button_y + 125,
            120,
            32
        )

        self.reset_fault_button.setGeometry(
            150,
            button_y + 125,
            120,
            32
        )

        self.emergency_vehicle_button.setGeometry(
            20,
            button_y + 170,
            250,
            32
        )

        # LOGS

        self.log_title.setGeometry(
            20,
            560,
            250,
            22
        )

        self.log_label.setGeometry(
            20,
            590,
            250,
            220
        )

    # UPDATE LABELS

    def update_hmi(
        self,
        lane1_count,
        lane2_count,
        divider_status,
        mode,
        sensor1,
        sensor2,
        prediction
    ):

        self.lane1_label.setText(
            f"Lane1 Density : {lane1_count}"
        )

        self.lane2_label.setText(
            f"Lane2 Density : {lane2_count}"
        )

        self.divider_label.setText(
            f"Divider : {divider_status}"
        )

        self.mode_label.setText(
            f"Mode : {mode}"
        )

        self.sensor1_label.setText(
            f"Lane1 Sensor : {sensor1}"
        )

        self.sensor2_label.setText(
            f"Lane2 Sensor : {sensor2}"
        )

        self.prediction_label.setText(
            f"Prediction :\n{prediction}"
        )

    # UPDATE ALARM

    def update_alarm(
        self,
        alarm_text,
        color
    ):

        self.alarm_label.setText(
            alarm_text
        )

        self.alarm_label.setStyleSheet(f"""
            color: {color};
            font-size: 14px;
            font-weight: bold;
        """)

    # UPDATE LOGS

    def update_logs(self, logs):

        self.log_label.setText(
            "\n".join(logs)
        )