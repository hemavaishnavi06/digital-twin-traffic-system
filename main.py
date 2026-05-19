import sys

from PyQt5.QtWidgets import (
    QApplication,
    QWidget
)

from PyQt5.QtGui import (
    QPainter
)

from PyQt5.QtCore import (
    Qt,
    QTimer
)

from config import *

from data_logger import DataLogger
from plc_controller import PLCController
from fault_manager import FaultManager
from prediction_engine import PredictionEngine
from traffic_light_controller import TrafficLightController
from vehicle_manager import VehicleManager
from road_drawer import RoadDrawer
from analytics import AnalyticsManager
from hmi_panel import HMIPanel
from traffic_state_manager import TrafficStateManager
from splash_screen import SplashScreen

class TrafficWindow(QWidget):

    def __init__(self):

        super().__init__()

        # WINDOW

        self.resize(
            WINDOW_WIDTH,
            WINDOW_HEIGHT
        )

        self.setWindowTitle(
            WINDOW_TITLE
        )

        self.setFocusPolicy(
            Qt.StrongFocus
        )

        # ENGINES

        self.plc = PLCController()

        self.fault_manager = FaultManager()

        self.predictor = PredictionEngine()

        self.vehicle_manager = VehicleManager()

        self.road_drawer = RoadDrawer()

        self.analytics = AnalyticsManager()

        self.logger = DataLogger()

        self.hmi = HMIPanel(self)

        self.traffic_light = (
            TrafficLightController()
        )

        self.traffic_state = (
            TrafficStateManager()
        )

        # VARIABLES

        self.divider_offset = 0

        self.target_divider_position = 0

        self.controller_mode = "AUTO"

        self.status_message = "Balanced"

        self.prediction_status = "Analyzing..."

        self.signal_status = "GREEN"

        self.system_logs = []

        self.emergency_vehicle = False

        # BUTTON CONNECTIONS

        self.hmi.auto_button.clicked.connect(
            self.activate_auto_mode
        )

        self.hmi.manual_button.clicked.connect(
            self.activate_manual_mode
        )

        self.hmi.emergency_button.clicked.connect(
            self.activate_emergency_mode
        )

        self.hmi.motor_fault_button.clicked.connect(
            self.activate_motor_fault
        )

        self.hmi.sensor_fault_button.clicked.connect(
            self.activate_sensor_fault
        )

        self.hmi.comm_fault_button.clicked.connect(
            self.activate_comm_fault
        )

        self.hmi.reset_fault_button.clicked.connect(
            self.reset_faults
        )

        self.hmi.emergency_vehicle_button.clicked.connect(
            self.activate_emergency_vehicle
        )

        # PANEL

        self.hmi.update_geometry(
            self.height()
        )

        # TIMER

        self.timer = QTimer()

        self.timer.timeout.connect(
            self.update_simulation
        )

        self.timer.start(
            TIMER_INTERVAL
        )

        # INITIAL LOG

        self.add_log(
            "SYSTEM STARTED"
        )

    # RESIZE

    def resizeEvent(self, event):

        self.hmi.update_geometry(
            self.height()
        )

    # LOGS

    def add_log(self, message):

        if len(self.system_logs) == 0 or \
           self.system_logs[-1] != message:

            self.system_logs.append(
                message
            )

        if len(self.system_logs) > MAX_LOGS:

            self.system_logs.pop(0)

        self.hmi.update_logs(
            self.system_logs
        )

    # MODES

    def activate_auto_mode(self):

        self.controller_mode = "AUTO"

        self.add_log(
            "AUTO MODE"
        )

    def activate_manual_mode(self):

        self.controller_mode = "MANUAL"

        self.add_log(
            "MANUAL MODE"
        )

    def activate_emergency_mode(self):

        self.controller_mode = "EMERGENCY"

        self.target_divider_position = (
            MAX_DIVIDER_SHIFT
        )

        self.add_log(
            "EMERGENCY MODE"
        )

    # EMERGENCY VEHICLE

    def activate_emergency_vehicle(self):

        self.emergency_vehicle = True

        self.vehicle_manager.add_emergency_vehicle()

        self.target_divider_position = (
            MAX_DIVIDER_SHIFT
        )

        self.add_log(
            "AMBULANCE DETECTED"
        )

    # FAULTS

    def activate_motor_fault(self):

        self.fault_manager.activate_motor_fault()

        self.add_log(
            "MOTOR FAULT"
        )

    def activate_sensor_fault(self):

        self.fault_manager.activate_sensor_fault()

        self.add_log(
            "SENSOR FAULT"
        )

    def activate_comm_fault(self):

        self.fault_manager.activate_communication_fault()

        self.add_log(
            "COMM FAULT"
        )

    def reset_faults(self):

        self.fault_manager.reset_faults()

        self.add_log(
            "FAULTS RESET"
        )

    # KEYBOARD

    def keyPressEvent(self, event):

        if self.controller_mode == "MANUAL":

            if event.key() == Qt.Key_Left:

                self.target_divider_position -= 40

                self.add_log(
                    "LEFT SHIFT"
                )

            elif event.key() == Qt.Key_Right:

                self.target_divider_position += 40

                self.add_log(
                    "RIGHT SHIFT"
                )

    # UPDATE

    def update_simulation(self):

        screen_height = self.height()

        # TRAFFIC LIGHT

        self.signal_status = (
            self.traffic_light.update_signal()
        )

        # EMERGENCY SIGNAL PRIORITY

        if self.controller_mode == "EMERGENCY":

            self.signal_status = "GREEN"

        # MOVE VEHICLES

        self.vehicle_manager.move_vehicles(
            screen_height,
            self.signal_status
        )

        # TRAFFIC COUNTS

        lane1_count, lane2_count = (

            self.vehicle_manager.get_lane_counts()
        )

        # DEFAULT

        traffic_text = "Equal Traffic"

        # EMERGENCY MODE

        if self.controller_mode == "EMERGENCY":

            self.target_divider_position = (
                MAX_DIVIDER_SHIFT
            )

            self.status_message = (
                "Emergency Lane Active"
            )

            traffic_text = (
                "Emergency Priority"
            )

        # NORMAL PLC CONTROL

        elif not self.fault_manager.communication_fault:

            if self.controller_mode == "AUTO":

                status_code, traffic_text = (

                    self.traffic_state.process_traffic(

                        lane1_count,

                        lane2_count
                    )
                )

                self.status_message = (

                    self.plc.process_traffic(

                        status_code
                    )
                )

                self.target_divider_position = (

                    self.plc.target_divider_position
                )

        # AMBULANCE PRIORITY

        if self.emergency_vehicle:

            self.target_divider_position = (
                MAX_DIVIDER_SHIFT
            )

            self.status_message = (
                "Priority Lane Active"
            )

            traffic_text = (
                "Ambulance Detected"
            )

        # MOTOR

        if not self.fault_manager.motor_fault:

            if self.divider_offset < self.target_divider_position:

                self.divider_offset += (
                    DIVIDER_MOVE_SPEED
                )

            elif self.divider_offset > self.target_divider_position:

                self.divider_offset -= (
                    DIVIDER_MOVE_SPEED
                )

        # ANALYTICS

        self.analytics.update_history(
            lane1_count,
            lane2_count,
            self.divider_offset
        )

        # PREDICTION

        self.prediction_status = (

            self.predictor.predict(

                self.analytics.lane1_history,

                self.analytics.lane2_history
            )
        )

        # SENSOR STATUS

        if self.fault_manager.sensor_fault:

            lane1_sensor = "ERROR"

            lane2_sensor = "ERROR"

        else:

            lane1_sensor = "ACTIVE"

            lane2_sensor = "ACTIVE"

        # HMI UPDATE

        self.hmi.update_hmi(

            lane1_count,

            lane2_count,

            traffic_text,

            self.controller_mode,

            lane1_sensor,

            lane2_sensor,

            self.prediction_status
        )

        # ALARMS

        if self.fault_manager.motor_fault:

            self.hmi.update_alarm(
                "ALARM : MOTOR FAILURE",
                "red"
            )

        elif self.fault_manager.sensor_fault:

            self.hmi.update_alarm(
                "ALARM : SENSOR FAILURE",
                "orange"
            )

        elif self.fault_manager.communication_fault:

            self.hmi.update_alarm(
                "ALARM : COMM LOST",
                "yellow"
            )

        elif self.emergency_vehicle:

            self.hmi.update_alarm(
                "ALARM : AMBULANCE PRIORITY",
                "cyan"
            )

        elif self.controller_mode == "EMERGENCY":

            self.hmi.update_alarm(
                "ALARM : EMERGENCY MODE",
                "cyan"
            )

        else:

            self.hmi.update_alarm(
                "ALARM : NORMAL",
                "lime"
            )

        # LOGGER

        self.logger.log_data(

            lane1_count,

            lane2_count,

            self.divider_offset,

            self.controller_mode,

            self.hmi.alarm_label.text(),

            self.prediction_status
        )

        self.update()

    # DRAW

    def paintEvent(self, event):
        painter = QPainter(self)
        width = self.width()
        height = self.height()

        # ROAD
        self.road_drawer.draw_road(
            painter,
            width,
            height
        )

        # TRAFFIC LIGHT
        self.road_drawer.draw_traffic_light(
            painter,
            self.signal_status
        )

        # DIVIDER POSITION
        road_width = width - ROAD_START
        divider_x = (
            ROAD_START
            + road_width // 2
            + self.divider_offset
        )

        # DIVIDER
        self.road_drawer.draw_divider(
            painter,
            divider_x,
            height
        )

        # VEHICLES
        self.road_drawer.draw_vehicles(
            painter,
            self.vehicle_manager.left_cars,
            self.vehicle_manager.right_cars,
            divider_x,
            width
        )

        # ANALYTICS
        self.analytics.draw_analytics(
            painter,
            width
        )

# START
app = QApplication(sys.argv)
window = TrafficWindow()
splash = SplashScreen(window)
splash.show()
sys.exit(app.exec_())