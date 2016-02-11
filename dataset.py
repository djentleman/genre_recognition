import utils.track as track

class Dataset:
    def __init__(self):
        self.data = []

    def addTrack(self, track):
        self.data.append(track)

    def addPath(self, path):
        self.data.append(track.Track(path))

    def merge(self, extDataset):
        self.data += extDataset.data

    def exportAsCSV(self):
        pass # todo

    def exportAsArff(self):
        pass # todo

    def dump(self):
        for track in self.data:
            track.dump()

    def plot(self):
        for track in self.data:
            track.plotWaveform()


    
