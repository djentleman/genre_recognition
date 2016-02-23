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
        self.averageFFT = []
        self.BPM = 0
        self.length = 0
        self.framerate = 0
        #Extract Raw Audio from Wav File
        self.getFeatures()

    def getSongFeatures(self):
        self.length = self.wave.duration_seconds
        self.framerate = self.wave.frame_rate
        # this should return an array or a dict
        

    def getFFTData(self):
        cFeatures = []
        ffts = []
        chunks = []
        for i in range(int(self.length * 4)):
            chunks.append(self.wave[i*250:(i+1)*250])
        for chunk in chunks:
            cFeatures.append(chunk.get_array_of_samples())
        # loop over cFeatures, run FFT to make data more useful
        # first get the frequency axis
        freq = map(lambda x: x * self.framerate,
                   numpy.fft.fftfreq(len(cFeatures[0])))
        # we need crop fft between 20 and 5000hz
        # we need to find the relevant indexes
        cropIndexLower = getIndex(freq, 20)
        cropIndexUpper = getIndex(freq, 5000)
        for sample in cFeatures:
            fft = numpy.fft.fft(sample).real
            processedFFT = abs(fft)[cropIndexLower:cropIndexUpper]
            ffts.append(processedFFT)
        ffts = numpy.asarray(ffts)
        return ffts.mean(axis=0)

    def plotAverageFFT(self):
        plot(self.averageFFT)
        
    def getFeatures(self):
        self.songFeatures = self.getSongFeatures()
        self.averageFFT = self.getFFTData()
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
    w.plotAverageFFT()
