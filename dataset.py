import utils.track as track

class Dataset:
    def __init__(self, csvPath):
        self.data = []
        self.path = csvPath

    def addTrack(self, tr):
        open(self.path, 'a').write(",".join([str(t) for t in tr.getFeatureSet()]) + '\n')

    def addPath(self, path):
        tr = track.Track(path)
        self.addTrack(tr)

    def readCsv(self):
        pass
        #todo



    
