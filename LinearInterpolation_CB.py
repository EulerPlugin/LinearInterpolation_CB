import numpy as np

class LinearInterpolation():
    def __call__(self, value, index):
        low = int(index)

        high = int(np.ceil(index))

        if low == high:
            return value[low]
        
        a = index - low

        return a * value[high % value.shape[0]] + (1 - a) * value[low]
    
def power_of_2(x):
    return int(2 ** np.ceil(np.log2(x)))

class CircularBuffer():
    def __init__(self, size, delay):
        size = power_of_2(size)
        self._LI = LinearInterpolation()
        self._buffer = np.zeros((size, ))
        self._write_pointer = 0.0
        self._read_pointer = (self._write_pointer - delay) % self._buffer.shape[0]
    
    def write_sample(self, x):
        self._buffer[int(self._write_pointer)] = x
        next_write = (self._write_pointer + 1) % self._buffer.shape[0]
        if next_write == self._read_pointer:
            raise Exception("Overrun")
        self._write_pointer = next_write

    def read_sample(self):
        if self._read_pointer == self._write_pointer:
            raise Exception("Underrun")
        sample = self._LI(self._buffer, self._read_pointer)
        self._read_pointer = (self._read_pointer + 1) % self._buffer.shape[0]
        return sample





