class TrafficLightController:

    def __init__(self):

        self.signal_state = "GREEN"

        self.counter = 0

    # UPDATE SIGNAL

    def update_signal(self):

        self.counter += 1

        # GREEN
        # ~25 seconds

        if self.counter < 850:

            self.signal_state = "GREEN"

        # YELLOW
        # ~5 seconds

        elif self.counter < 1000:

            self.signal_state = "YELLOW"

        # RED
        # ~8 seconds

        elif self.counter < 1260:

            self.signal_state = "RED"

        else:

            self.counter = 0

        return self.signal_state