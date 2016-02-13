# waveform utils
from pydub import AudioSegment
import sys
import scipy.fftpack
import matplotlib.pyplot as plt
import numpy


class Waveform():
    def __init__(self, path):
        self.path = path
        self.wave = song = AudioSegment.from_wav(path)
        self.chunks = []
        self.chunkFeatures = []
        self.songFeatures = []
        #Extract Raw Audio from Wav File
        self.getFeatures()

    def splitWaves(self):
        for i in range(int(self.length * 4)):
            self.chunks.append(self.wave[i*250:(i+1)*250])

    def getSongFeatures(self):
        self.length = self.wave.duration_seconds
        self.framerate = self.wave.frame_rate
        # this should return an array or a dict
        

    def getChunkFeatures(self):
        cFeatures = []
        ffts = []
        for chunk in self.chunks:
            cFeatures.append(chunk.get_array_of_samples())
        # loop over cFeatures, run FFT to make data more useful
        # sample spacing
        T = 1.0 / 800.0
        for sample in cFeatures:
            fft = scipy.fftpack.fft(sample).real
            ffts.append(abs(fft[:len(fft)/2]))
        return ffts

    def getAverageFFT(self, plot=False):
        ffts = numpy.asarray(self.chunkFeatures)
        self.averageFFT = ffts.mean(axis=0)

    def plotAverageFFT(self):
        self.getAverageFFT()
        plot(self.averageFFT)
        
    def getFeatures(self):
        self.songFeatures = self.getSongFeatures()
        self.splitWaves() # split the wave into one second chunks
        self.chunkFeatures = self.getChunkFeatures()
        # merge sets together

def plot(data):
    plt.cla()
    plt.plot(data)
    plt.show()

if __name__ == "__main__":
    w = Waveform('C:/Users/Todd/tmp.wav')
    plot(w.averageFFT)
