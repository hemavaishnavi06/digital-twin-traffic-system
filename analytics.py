from PyQt5.QtGui import (
    QColor,
    QPen
)

from PyQt5.QtCore import (
    QPoint,
    Qt
)

from config import *


class AnalyticsManager:

    def __init__(self):

        self.lane1_history = []

        self.lane2_history = []

        self.divider_history = []

    # UPDATE HISTORY

    def update_history(
        self,
        lane1_count,
        lane2_count,
        divider_position
    ):

        self.lane1_history.append(
            lane1_count
        )

        self.lane2_history.append(
            lane2_count
        )

        self.divider_history.append(
            divider_position
        )

        # LIMIT HISTORY

        if len(self.lane1_history) > 60:

            self.lane1_history.pop(0)

        if len(self.lane2_history) > 60:

            self.lane2_history.pop(0)

        if len(self.divider_history) > 60:

            self.divider_history.pop(0)

    # DRAW GRAPH

    def draw_graph(
        self,
        painter,
        history,
        x,
        y,
        width,
        height,
        color
    ):

        if len(history) < 2:

            return

        painter.setPen(

            QPen(
                QColor(*color),
                3
            )
        )

        max_value = max(history)

        if max_value == 0:

            max_value = 1

        step_x = width / (
            len(history) - 1
        )

        points = []

        for i, value in enumerate(history):

            graph_x = x + i * step_x

            graph_y = (

                y + height
                - (value / max_value)
                * height
            )

            points.append(

                QPoint(
                    int(graph_x),
                    int(graph_y)
                )
            )

        for i in range(len(points) - 1):

            painter.drawLine(

                points[i],

                points[i + 1]
            )

    # DRAW ANALYTICS

    def draw_analytics(
        self,
        painter,
        width
    ):

        panel_x = width - 380

        panel_y = 20

        panel_width = 350

        panel_height = 320

        # PANEL

        painter.fillRect(

            panel_x,

            panel_y,

            panel_width,

            panel_height,

            QColor(20,20,20)
        )

        painter.setPen(

            QPen(Qt.cyan, 2)
        )

        painter.drawRect(

            panel_x,

            panel_y,

            panel_width,

            panel_height
        )

        # TITLE

        painter.setPen(Qt.white)

        painter.drawText(

            panel_x + 15,

            panel_y + 25,

            "TRAFFIC ANALYTICS"
        )

        graph_x = panel_x + 20

        graph_width = 300

        graph_height = 55

        # LANE1 TITLE

        painter.setPen(Qt.green)

        painter.drawText(

            graph_x,

            panel_y + 50,

            "Lane1 Density"
        )

        # LANE1 GRAPH

        self.draw_graph(

            painter,

            self.lane1_history,

            graph_x,

            panel_y + 60,

            graph_width,

            graph_height,

            LEFT_CAR_COLOR
        )

        # LANE2 TITLE

        painter.setPen(

            QColor(255,120,120)
        )

        painter.drawText(

            graph_x,

            panel_y + 145,

            "Lane2 Density"
        )

        # LANE2 GRAPH

        self.draw_graph(

            painter,

            self.lane2_history,

            graph_x,

            panel_y + 155,

            graph_width,

            graph_height,

            (255,120,120)
        )

        # DIVIDER TITLE

        painter.setPen(Qt.yellow)

        painter.drawText(

            graph_x,

            panel_y + 240,

            "Divider Position"
        )

        # DIVIDER GRAPH

        self.draw_graph(

            painter,

            self.divider_history,

            graph_x,

            panel_y + 250,

            graph_width,

            graph_height,

            YELLOW
        )