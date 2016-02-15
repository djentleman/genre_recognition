# -*- coding: utf-8 -*-
import utils.track as track
import io

class Dataset:
    def __init__(self, csvPath):
        self.data = []
        self.path = csvPath

    def addTrack(self, tr):
        strs = [unicodeConvert(t) for t in tr.getFeatureSet()]
        writeStr = ','.join(strs) + '\n'
        io.open(self.path, 'a').write(writeStr)
    
    def addPath(self, path):
        tr = track.Track(path)
        self.addTrack(tr)

    def readCsv(self):
        pass
        #todo


def unicodeConvert(s):
    # not proud of this but it works :^)
    try:
        return unicode(s, 'utf-8')
    except:
        try:
            return unicode(str(s), 'utf-8')
        except:
            return s
