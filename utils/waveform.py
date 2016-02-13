# waveform utils
from pydub import AudioSegment
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
        # first get the frequency axis
        freq = map(lambda x: x * self.framerate,
                   numpy.fft.fftfreq(len(cFeatures[0])))
        # we need crop fft between 20 and 20000hz
        # we need to find the relevant indexes
        cropIndexLower = getIndex(freq, 20)
        cropIndexUpper = getIndex(freq, 10000)
        for sample in cFeatures:
            fft = numpy.fft.fft(sample).real
            processedFFT = abs(fft)[cropIndexLower:cropIndexUpper]
            ffts.append(processedFFT)
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
    plt.clf()
    plt.plot(data)
    plt.show()

def getIndex(array, toFind):
    # only works for sorted arrays, eg ftt freq axis
    for val in array:
        if toFind <= val:
            return array.index(val)

if __name__ == "__main__":
    w = Waveform('C:/Users/Todd/tmp.wav')
    w.getAverageFFT()
    plot(w.averageFFT)
