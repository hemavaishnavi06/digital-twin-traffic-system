class PredictionEngine:

    def predict(
        self,
        lane1_history,
        lane2_history
    ):

        if len(lane1_history) < 10:
            return "Analyzing..."

        recent_lane1 = lane1_history[-5:]
        recent_lane2 = lane2_history[-5:]

        avg1 = sum(recent_lane1) / len(recent_lane1)
        avg2 = sum(recent_lane2) / len(recent_lane2)

        if avg1 > avg2 + 2:
            return "Future Congestion : Lane1"

        elif avg2 > avg1 + 2:
            return "Future Congestion : Lane2"

        else:
            return "Traffic Stable"