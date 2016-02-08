# mp3 parsing library
import eyed3 # used for getting mp3 metadata
import utils.lastfm as lastfm
import utils.wavconvert as wavconvert

class Track:
    def __init__(self, path=""):
        if path == "":
            # metadata attributes
            self.name = ""
            self.artist = ""
            self.album = ""
            self.path = ""
            # lastfm tags
            self.tags = []
        else:
            self.getMetadata(path)
            self.getGenreTags()
            
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

    def getGenreTags(self):
        self.tags = lastfm.getTrackTags(self.artist, self.name)

    def analyseTrack(self):
        # first convert to wav
        if (wavconvert.convertFile(self.path)):
            # TODO: extract features from the wav file
            wavconvert.destroyTmp()
        else:
            print "Err: File could not be converted into wav"
        

    def dump(self):
        print "Artist: " + self.artist
        print "Album: " + self.album
        print "Track: " + self.name
        print "Path: " + self.path
        for tag in self.tags:
            print "     " + tag
        print "---------------------------"
        

if __name__ == "__main__":
    path = "C:\Users\Todd\Music\song.mp3"
    mp3 = Track(path)
    mp3.dump()
    mp3.analyseTrack()
