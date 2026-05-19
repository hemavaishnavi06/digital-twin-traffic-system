from config import *
class PLCController:

    def __init__(self):

        self.target_divider_position = 0

    # PROCESS TRAFFIC

    def process_traffic(
        self,
        status_code
    ):

        # EQUAL TRAFFIC

        if status_code == 0:

            self.target_divider_position = 0

            return "Divider Center"

        # LANE1 HIGH

        elif status_code == 1:

            self.target_divider_position = (
                HIGH_TRAFFIC_SHIFT
            )

            return "Shift Right"

        # LANE2 HIGH

        elif status_code == 2:

            self.target_divider_position = (
                -HIGH_TRAFFIC_SHIFT
            )

            return "Shift Left"