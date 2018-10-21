import numpy as np
import matplotlib.pyplot as plt
from collections import deque
import pyaudio
from scipy import signal
from my_midgets.midget import Midget

plt.ion()


class BarkMidget(Midget):
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 1000
    CHUNK = RATE//5
    FRAME_SIZE = 5
    DOWNSAMPLE_FACTOR = 4

    def __init__(self):
        super().__init__()
        self.pyaudio = pyaudio.PyAudio()
        self.stream = self.pyaudio.open(format=self.FORMAT,
                                        channels=self.CHANNELS,
                                        rate=self.RATE,
                                        input=True,
                                        frames_per_buffer=self.CHUNK)
        
        self.frames = deque(maxlen=(self.RATE * self.FRAME_SIZE))

    def listen(self):
        num_peaks = 0
        while True:
            raw_data = self.stream.read(self.CHUNK)
            data = np.fromstring(raw_data, dtype=np.int16)
            data = signal.decimate(data, self.DOWNSAMPLE_FACTOR)
            num_peaks += len(signal.find_peaks(data, threshold=20000))
            self.frames.extend(list(data))
            
    def run(self):
        self.listen()