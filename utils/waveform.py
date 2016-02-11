# waveform utils
import matplotlib.pyplot as plot
import numpy
import wave
import sys

class Waveform():
    def __init__(self, path):
        self.path = path
        self.wave = wave.open(path, 'r')
        #Extract Raw Audio from Wav File
        self.signal = numpy.fromstring(self.wave.readframes(-1), 'Int16')
        self.nochannels = self.wave.getnchannels()

    def plot(self):
        plot.title('Signal Wave...')
        plot.plot(self.signal)
        plot.show()

    def close(self):
        self.wave.close()
