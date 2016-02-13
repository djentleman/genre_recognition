# mp3 parsing library
import eyed3 # used for getting mp3 metadata
import lastfm
import wavconvert
import waveform

class Track:
    def __init__(self, path=""):
        self.metadata = False
        # metadata attributes
        self.name = ""
        self.artist = ""
        self.album = ""
        self.path = ""
        self.waveform = None
        # lastfm tags
        self.tags = []
        if path != "":
            self.getMetadata(path)
        if self.metadata:
            self.getGenreTags()
        self.analyseTrack()
            
    def getMetadata(self, path):
        self.path = path
        extension = self.path.split(".")[-1]
        if extension == "mp3":
            self.getMetadataMp3()
        # TODO: metadata getters for wav, flv and ogg
        
    def getMetadataMp3(self):
        tag = eyed3.load(self.path).tag
        self.name = tag.title
        self.artist = tag.artist
        self.album = tag.album
        self.metadata = True

    def getGenreTags(self):
        self.tags = lastfm.getTopTags(self.artist, self.name)

    def analyseTrack(self, plotWaveform=False):
        # first convert to wav
        if (wavconvert.convertFile(self.path)):
            self.waveform = waveform.Waveform("tmp.wav")
            if plotWaveform:
                self.plotWaveform()
            wavconvert.destroyTmp()
        else:
            print "Err: File could not be converted into wav"
            
    def plotFFT(self):
        self.waveform.plotAverageFFT()

    def dump(self):
        print "Artist: " + self.artist
        print "Album: " + self.album
        print "Track: " + self.name
        print "Path: " + self.path
        for tag in self.tags:
            print "     " + tag
        print "---------------------------"

def isValidPath(path):
    ext = path.split(".")[-1]
    return (ext == "wav" or
            ext == "mp3" or
            ext == "ogg" or
            ext == "flv")
        

if __name__ == "__main__":
    path = "C:\Users\Todd\Music\song.mp3"
    song = Track(path)
    song.dump()
    song.plotFFT()
    path2 = 'C:\Users\Todd\Documents\Metallica/01 Enter Sandman.mp3'
    song = Track(path2)
    song.dump()
    song.plotFFT()
    path3 = 'C:\Users\Todd\Documents\Iglooghost\Chinese Nu Year/2 Mametchi Usohachi.mp3'
    song = Track(path3)
    song.dump()
    song.plotFFT()
    
    
    
