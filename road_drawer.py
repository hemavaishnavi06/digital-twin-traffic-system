from PyQt5.QtGui import (
    QColor,
    QPen,
    QBrush
)

from PyQt5.QtCore import Qt
from config import *

class RoadDrawer:
    # ROAD
    def draw_road(
        self,
        painter,
        width,
        height
    ):
        painter.fillRect(
            ROAD_START,
            0,
            width - ROAD_START,
            height,
            QColor(*ROAD_COLOR)
        )
    # DIVIDER
    def draw_divider(
        self,
        painter,
        divider_x,
        height
    ):
        painter.setPen(
            QPen(
                Qt.yellow,
                DIVIDER_WIDTH
            )
        )
        painter.drawLine(
            divider_x,
            0,
            divider_x,
            height
        )
    # VEHICLES
    def draw_vehicles(
        self,
        painter,
        left_cars,
        right_cars,
        divider_x,
        width
    ):
        # LEFT SIDE
        left_center = (
            ROAD_START
            + (divider_x - ROAD_START) // 2
        )
        for car in left_cars:
            x = left_center + car["x_offset"]
            # EMERGENCY VEHICLE
            if "emergency" in car:
                painter.setBrush(
                    QColor(0,150,255)
                )
            else:

                painter.setBrush(

                    QColor(*LEFT_CAR_COLOR)
                )

            painter.drawRect(

                x,

                car["y"],

                CAR_WIDTH,

                CAR_HEIGHT
            )

        # RIGHT SIDE

        right_center = (

            divider_x
            + (width - divider_x) // 2
        )

        for car in right_cars:

            x = right_center + car["x_offset"]

            painter.setBrush(

                QColor(*RIGHT_CAR_COLOR)
            )

            painter.drawRect(

                x,

                car["y"],

                CAR_WIDTH,

                CAR_HEIGHT
            )

    # TRAFFIC LIGHT

    def draw_traffic_light(
        self,
        painter,
        signal
    ):

        # BODY

        painter.setBrush(
            QColor(30,30,30)
        )

        painter.drawRect(
            340,
            40,
            60,
            180
        )

        # RED

        if signal == "RED":

            painter.setBrush(
                QColor(255,0,0)
            )

        else:

            painter.setBrush(
                QColor(80,0,0)
            )

        painter.drawEllipse(
            355,
            55,
            30,
            30
        )

        # YELLOW

        if signal == "YELLOW":

            painter.setBrush(
                QColor(255,255,0)
            )

        else:

            painter.setBrush(
                QColor(80,80,0)
            )

        painter.drawEllipse(
            355,
            105,
            30,
            30
        )

        # GREEN
        if signal == "GREEN":
            painter.setBrush(
                QColor(0,255,0)
            )

        else:
            painter.setBrush(
                QColor(0,80,0)
            )

        painter.drawEllipse(
            355,
            155,
            30,
            30
        )

    # ANALYTICS PANEL

    def draw_analytics_panel(
        self,
        painter,
        analytics_x,
        analytics_y
    ):

        painter.fillRect(
            analytics_x,
            analytics_y,
            ANALYTICS_PANEL_WIDTH,
            ANALYTICS_PANEL_HEIGHT,
            QColor(20,20,20)
        )

        painter.setPen(
            QPen(Qt.cyan, 2)
        )

        painter.drawRect(
            analytics_x,
            analytics_y,
            ANALYTICS_PANEL_WIDTH,
            ANALYTICS_PANEL_HEIGHT
        )

        painter.setPen(Qt.white)
        painter.drawText(
            analytics_x + 15,
            analytics_y + 20,
            "TRAFFIC ANALYTICS"
        )