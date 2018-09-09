import numpy
import pyaudio
from scipy import signal
from matplotlib import pyplot
from my_midgets.midget import Midget

class BarkMidget(Midget):

    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 44100
    CHUNK = 1024

    def __init__(self):
        self.pyaudio = pyaudio.PyAudio()
        self.stream = self.pyaudio.open(format=self.FORMAT,
                                        channels=self.CHANNELS,
                                        rate=self.RATE,
                                        input=True,
                                        frames_per_buffer=self.CHUNK)

    def listen(self, duration=5):
        frames = []
        for _ in range(0, int(self.RATE / self.CHUNK * duration)):
            raw_data = self.stream.read(self.CHUNK)
            data = numpy.fromstring(raw_data, dtype=numpy.int16)
            frames.append(data)

        full_data = numpy.hstack(frames)
        peaks = signal.find_peaks(full_data, threshold=20000)
        print(len(peaks))
        pyplot.plot(full_data)
        pyplot.show()

BarkMidget().listen()