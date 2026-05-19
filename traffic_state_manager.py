class TrafficStateManager:

    def __init__(self):

        self.status_code = 0

        self.status_text = "Equal Traffic"

    # PROCESS TRAFFIC

    def process_traffic(
        self,
        lane1_count,
        lane2_count
    ):

        diff = lane1_count - lane2_count

        # KEEP EQUAL IF DIFFERENCE <= 10

        if abs(diff) <= 5:

            self.status_code = 0

            self.status_text = (
                "Equal Traffic"
            )

        # LANE1 HIGH

        elif diff > 5:

            self.status_code = 1

            self.status_text = (
                "High Traffic : Lane1"
            )

        # LANE2 HIGH

        elif diff < -5:

            self.status_code = 2

            self.status_text = (
                "High Traffic : Lane2"
            )

        return (

            self.status_code,

            self.status_text
        )