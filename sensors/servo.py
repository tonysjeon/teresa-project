import time
import math
from util.memory_manager import SharedMemoryManager


def degrees_to_radians(degrees):
    return degrees * (math.pi / 180)


# User facing servo
class Servo:
    def __init__(self, name):
        self.shared_memory = SharedMemoryManager(name, array_size=1)

    def write(self, position):
        self.shared_memory.write([position])


# Simulated servo
class SimServo:
    def __init__(self, name):
        self.shared_memory = SharedMemoryManager(name, array_size=1)
        self.speed = 150
        self.position = 0
        self.target = 0
        self.last_update = time.time()

    def set_target(self, target_position):
        self.target = math.ceil(target_position)

    def update_position(self):
        now = time.time()
        elapsed = now - self.last_update
        self.last_update = now

        max_step = self.speed * elapsed
        distance = self.target - self.position

        if abs(distance) <= max_step:
            self.position = self.target
        else:
            self.position += max_step if distance > 0 else -max_step

    def update(self):
        angle = self.shared_memory.read()
        self.set_target(angle)
        self.update_position()

    def get_position(self):
        return degrees_to_radians(self.position)
