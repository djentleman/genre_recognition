import soundcloud
import ConfigParser
import requests
from pydub import AudioSegment

class _soundcloud_:
    clientID = ""
    clientSecret = ""
    client = None

    def __init__(self, clientID="", clientSecret=""):

        # If we have an empty or invalid clientID
        if self.clientID is "" or self.clientID is not str:
            # Read in the apikeys.ini file
            configReader = ConfigParser.ConfigParser()
            configReader.read("..\\conf\\apikeys.ini")

            # Initialise the clientID and clientSecret from the .ini file
            self.clientID = configReader.get("soundcloud", "clientid")

        # If we have an empty or invalid clientSecret
        if self.clientSecret is "" or self.clientSecret is not str:
            # Read in the apikeys.ini file
            configReader = ConfigParser.ConfigParser()
            configReader.read("..\\conf\\apikeys.ini")

            # Initialise the clientID and clientSecret from the .ini file
            self.clientSecret = configReader.get("soundcloud", "clientsecret")

        self.client = soundcloud.Client(client_id=self.clientID)

    # getSongs - Returns an array of JSON objects which contains metadata for all search results
    # that were found for query 'query'.
    def getSongs(self, query=""):
        return [sound.fields() for sound in self.client.get('/tracks', q=query)]

    def streamSong(self, streamURL=""):
        if streamURL is "":
            return

        audioStream = requests.get('https://api.soundcloud.com/tracks/227318766/stream' + "?client_id=" + self.clientID, stream=True)

        print audioStream.content

if __name__ == "__main__":
    thing = _soundcloud_()

    thing.streamSong("ayy")