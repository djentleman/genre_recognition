# waveform utils
from pydub import AudioSegment
import sys

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
        for i in range(int(self.length)):
            self.chunks.append(self.wave[i*1000:(i+1)*1000])

    def getSongFeatures(self):
        self.length = self.wave.duration_seconds
        self.framerate = self.wave.frame_rate
        # this should return an array or a dict
        

    def getChunkFeatures(self):
        cFeatures = []
        for chunk in self.chunks:
            cFeatures.append(chunk.get_array_of_samples())
        return cFeatures
        

    def getFeatures(self):
        self.songFeatures = self.getSongFeatures()
        self.splitWaves() # split the wave into one second chunks
        self.chunkFeatures = self.getChunkFeatures()
        # merge sets together

if __name__ == "__main__":
    w = Waveform('C:/Users/Todd/tmp.wav')
