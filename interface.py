from sensors.imu import SimulatedIMU
from sensors.servo import Servo
import time
import numpy as np

# Filter class
class ComplementaryFilter:
    def __init__(self, alpha=0.98):
        self.alpha = alpha  # Weight for gyroscope data
        self.angle = 0.0    # Initial angle

    def update(self, gyro_data, accel_data, dt):
        # Integrate gyroscope data
        self.angle += gyro_data * dt
        # Fuse with accelerometer data
        self.angle = self.alpha * self.angle + (1 - self.alpha) * accel_data
        return self.angle

if __name__ == "__main__":
    # Setup
    imu = SimulatedIMU("data/sample_data.csv")
    yaw_servo = Servo("yaw")
    pitch_servo = Servo("pitch")

    # Initialize filters
    yaw_filter = ComplementaryFilter()
    pitch_filter = ComplementaryFilter()

if __name__ == "__main__":
    # Setup
    imu = SimulatedIMU("data/sample_data.csv")
    yaw_servo = Servo("yaw")
    pitch_servo = Servo("pitch")

    # Initialize filters
    yaw_filter = ComplementaryFilter()
    pitch_filter = ComplementaryFilter()

    # Loop
    while True:
        # Read from sensor
        imu.update()
        angles = imu.get_angles()  # pitch, roll, yaw
        gyro_data = imu.get_gyro()  # gyroscope data (pitch_rate, roll_rate, yaw_rate)
        accel_data = imu.get_accel()  # accelerometer data (pitch, roll)

        # Apply filters
        dt = 0.01  # Time step (adjust based on your IMU update rate)
        yaw_angle = yaw_filter.update(gyro_data[2], angles[2], dt)
        pitch_angle = pitch_filter.update(gyro_data[0], angles[0], dt)

        # Send command to servos
        yaw_servo.write(yaw_angle)
        pitch_servo.write(pitch_angle)

        time.sleep(dt)
