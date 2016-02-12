import soundcloud
import ConfigParser

class _soundcloud_:
    clientID = ""
    clientSecret = ""

    def __init__(self, clientID="", clientSecret=""):
        self.clientID = clientID
        self.clientSecret = clientSecret

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

    # getSongs - Returns a JSON array of data, which contains an array of all search results that were found
    # for query 'query'.
    def getSongs(self, query=""):
        return soundcloud.Client(client_id=self.clientID).get('/tracks', q=query)

if __name__ == "__main__":
    thing = _soundcloud_()