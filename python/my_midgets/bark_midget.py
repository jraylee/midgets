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

    def listen(self, duration=100):
        frames = deque(maxlen=(self.RATE * self.FRAME_SIZE))
        num_peaks = 0
        for _ in range(0, int(self.RATE / self.CHUNK * duration)):
            raw_data = self.stream.read(self.CHUNK)
            data = np.fromstring(raw_data, dtype=np.int16)
            data = signal.decimate(data, self.DOWNSAMPLE_FACTOR)
            num_peaks += len(signal.find_peaks(data, threshold=20000))
            frames.extend(list(data))
            plt.clf()
            plt.plot(frames)
            plt.pause(0.01)
        print(num_peaks)




BarkMidget().listen()