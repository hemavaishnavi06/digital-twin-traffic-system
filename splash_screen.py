from PyQt5.QtWidgets import (
    QWidget,
    QLabel,
    QVBoxLayout
)

from PyQt5.QtCore import (
    Qt,
    QTimer
)

from PyQt5.QtGui import (
    QFont
)


class SplashScreen(QWidget):

    def __init__(
        self,
        main_window
    ):

        super().__init__()

        self.main_window = main_window

        # WINDOW

        self.setWindowTitle(
            "ABB Digital Twin"
        )

        self.setFixedSize(
            700,
            400
        )

        self.setStyleSheet("""

            background-color: black;
            border: 3px solid cyan;
        """)

        # LAYOUT

        layout = QVBoxLayout()

        layout.setAlignment(
            Qt.AlignCenter
        )

        # TITLE

        title = QLabel(
            "DIGITAL TWIN PLATFORM"
        )

        title.setStyleSheet("""

            color: cyan;
        """)

        title.setFont(
            QFont(
                "Arial",
                24,
                QFont.Bold
            )
        )

        title.setAlignment(
            Qt.AlignCenter
        )

        # SUBTITLE

        subtitle = QLabel(
            "Adaptive Traffic Infrastructure"
        )

        subtitle.setStyleSheet("""

            color: white;
        """)

        subtitle.setFont(
            QFont(
                "Arial",
                18
            )
        )

        subtitle.setAlignment(
            Qt.AlignCenter
        )

        # DESCRIPTION

        description = QLabel(

            "Virtual Commissioning System\n"
            "PLC Logic + HMI Graphics Testing"
        )

        description.setStyleSheet("""

            color: lime;
        """)

        description.setFont(
            QFont(
                "Arial",
                14
            )
        )

        description.setAlignment(
            Qt.AlignCenter
        )

        # ADD WIDGETS

        layout.addWidget(title)

        layout.addSpacing(30)

        layout.addWidget(subtitle)

        layout.addSpacing(20)

        layout.addWidget(description)

        self.setLayout(layout)

        # TIMER

        QTimer.singleShot(
            5000,
            self.open_main_window
        )

    # OPEN MAIN WINDOW
    def open_main_window(self):
        self.main_window.show()
        self.close()