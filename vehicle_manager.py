import random
import time

from config import *


class VehicleManager:

    def __init__(self):

        self.left_cars = []

        self.right_cars = []

        # INITIAL COUNTS

        self.left_target_count = 15

        self.right_target_count = 15

        # TIMER

        self.last_update_time = time.time()

        self.next_update_interval = random.randint(
            10,
            25
        )

        # INITIAL VEHICLES

        self.generate_vehicles()

    # GENERATE VEHICLES

    def generate_vehicles(self):

        self.left_cars.clear()

        self.right_cars.clear()

        # LEFT VEHICLES

        for i in range(self.left_target_count):

            self.left_cars.append({

                "x_offset": random.randint(
                    -120,
                    120
                ),

                "y": random.randint(
                    0,
                    900
                )
            })

        # RIGHT VEHICLES

        for i in range(self.right_target_count):

            self.right_cars.append({

                "x_offset": random.randint(
                    -120,
                    120
                ),

                "y": random.randint(
                    0,
                    900
                )
            })

    # UPDATE TRAFFIC DENSITY

    def update_vehicle_density(self):

        current_time = time.time()

        elapsed = (
            current_time
            - self.last_update_time
        )

        # RANDOM UPDATE

        if elapsed > self.next_update_interval:

            # LEFT CHANGE

            left_change = random.randint(
                -4,
                4
            )

            self.left_target_count += (
                left_change
            )

            self.left_target_count = max(
                5,
                min(
                    40,
                    self.left_target_count
                )
            )

            # RIGHT CHANGE

            right_change = random.randint(
                -4,
                4
            )

            self.right_target_count += (
                right_change
            )

            self.right_target_count = max(
                5,
                min(
                    40,
                    self.right_target_count
                )
            )

            # REGENERATE VEHICLES

            self.generate_vehicles()

            # RESET TIMER

            self.last_update_time = (
                current_time
            )

            self.next_update_interval = (
                random.randint(10,25)
            )

    # MOVE VEHICLES

    def move_vehicles(
        self,
        screen_height,
        signal
    ):

        # UPDATE TRAFFIC

        self.update_vehicle_density()

        # SIGNAL CONTROL

        if signal == "RED":

            return

        elif signal == "YELLOW":

            speed = 2

        else:

            speed = CAR_SPEED

        # LEFT SIDE

        for car in self.left_cars:

            car["y"] -= speed

            if car["y"] < -80:

                car["y"] = (
                    screen_height + 50
                )

        # RIGHT SIDE

        for car in self.right_cars:

            car["y"] += speed

            if car["y"] > screen_height + 50:

                car["y"] = -80

    # COUNTS

    def get_lane_counts(self):

        return (

            len(self.left_cars),

            len(self.right_cars)
        )

    # EMERGENCY VEHICLE

    def add_emergency_vehicle(self):

        self.left_cars.append({

            "x_offset": 120,

            "y": 850,

            "emergency": True
        })