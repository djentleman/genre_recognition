# mp3 parsing library
import eyed3 # used for getting mp3 metadata
import lastfm

class MP3:
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
        tag = eyed3.load(path).tag
        self.name = tag.title
        self.artist = tag.artist
        self.album = tag.album
        self.path = path

    def getGenreTags(self):
        self.tags = lastfm.getTrackTags(self.artist, self.name)

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
    mp3 = MP3(path)
    mp3.dump()
