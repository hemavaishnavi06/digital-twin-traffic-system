class TrafficLightController:
    def __init__(self):
        self.signal_state = "GREEN"
        self.counter = 0

    # UPDATE SIGNAL
    def update_signal(self):
        self.counter += 1
        # GREEN
        # ~15 seconds
        if self.counter < 500:
            self.signal_state = "GREEN"
        # YELLOW
        # ~5 seconds
        elif self.counter < 650:
            self.signal_state = "YELLOW"
        # RED
        # ~15 seconds
        elif self.counter < 1000:
            self.signal_state = "RED"
        else:
            self.counter = 0
        return self.signal_state