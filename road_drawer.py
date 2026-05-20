from PyQt5.QtGui import (
    QColor,
    QPen
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

        # ROAD BODY

        painter.fillRect(

            ROAD_START,

            0,

            width - ROAD_START,

            height,

            QColor(*ROAD_COLOR)
        )

        # ROAD EDGES

        road_left = ROAD_START + 25

        road_right = width - 25

        # SOLID WHITE EDGE LINES

        painter.setPen(

            QPen(
                QColor(255,255,255),
                12
            )
        )

        # LEFT EDGE

        painter.drawLine(

            road_left,

            0,

            road_left,

            height
        )

        # RIGHT EDGE

        painter.drawLine(

            road_right,

            0,

            road_right,

            height
        )

        # FIXED CENTER

        fixed_center = (

            ROAD_START
            + (width - ROAD_START) // 2
        )

        # MOVE STRIPES FURTHER
        # INTO THE LANES

        left_stripe = (
            fixed_center - 340
        )

        right_stripe = (
            fixed_center + 340
        )

        # STRIPE STYLE

        painter.setPen(

            QPen(
                QColor(230,230,230),
                8
            )
        )

        stripe_height = 45

        stripe_gap = 35

        y = 0

        while y < height:

            # LEFT STRIPE

            painter.drawLine(

                left_stripe,

                y,

                left_stripe,

                y + stripe_height
            )

            # RIGHT STRIPE

            painter.drawLine(

                right_stripe,

                y,

                right_stripe,

                y + stripe_height
            )

            y += (
                stripe_height
                + stripe_gap
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

        # RED LIGHT

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

        # YELLOW LIGHT

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

        # GREEN LIGHT

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