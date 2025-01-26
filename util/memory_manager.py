from multiprocessing.shared_memory import SharedMemory
import numpy as np


class SharedMemoryManager:
    def __init__(self, name, type=np.float64, array_size=2):
        self.name = name
        self.size = array_size * np.dtype(np.float64).itemsize
        try:
            self.shm = SharedMemory(name=self.name)
        except:
            self.shm = SharedMemory(create=True, size=self.size, name=self.name)

        self.buffer = np.ndarray((array_size,), dtype=np.float64, buffer=self.shm.buf)
        self.open = True

    def close(self):
        if self.open:
            self.shm.close()
            self.open = False

    def read(self):
        return self.buffer[:]

    def write(self, data):
        self.buffer[:] = data

    def __del__(self):
        self.close()

    def get_buffer(self):
        return self.buffer
