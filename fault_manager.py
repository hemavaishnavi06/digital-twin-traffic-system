class FaultManager:
    def __init__(self):
        self.motor_fault = False
        self.sensor_fault = False
        self.communication_fault = False
    # =====================================================
    # MOTOR FAULT
    # =====================================================
    def activate_motor_fault(self):
        self.motor_fault = True
    # =====================================================
    # SENSOR FAULT
    # =====================================================
    def activate_sensor_fault(self):
        self.sensor_fault = True
    # =====================================================
    # COMMUNICATION FAULT
    # =====================================================
    def activate_communication_fault(self):
        self.communication_fault = True
    # =====================================================
    # RESET ALL
    # =====================================================
    def reset_faults(self):
        self.motor_fault = False
        self.sensor_fault = False
        self.communication_fault = False