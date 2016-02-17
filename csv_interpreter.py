# interpreter for csv file

# for test purposes - this whitelist will be loaded from a config file
# we can use this to control how many genres we will classify, for instance
# replacing the whitelist with ['classical', 'metal'] will allow for binary
# classification
def getWhitelist():
    return   ['instrumental hip-hop', 'thrash metal',
             'chillwave', 'ambient', 'hard rock',
             'seapunk',
             'electronica', 'electronic', 'nostalgia', 'Ballad', 'post-trap',
             'chillout', 'techno',
             'trip-hop', 'downtempo', 'metallica', 'psychedelic', 'chill',
             'breakcore', 'metal', 'best track ever',
             'idm', 'trap', 'rock', 'Acid', 'experimental']

def readCsv(path):
    return [row.split(",") for row in open(path, 'r').read().split("\n")]

def handleCsv(path = "csv.csv"):
    # load csv into array
    csv = readCsv(path)
    # remove invalid records
    csv = filter(lambda x: len(x) > 2495, csv)
    # reformat output vector
    inputVectors = [row[:2495] for row in csv]
    outputData = [row[-5:] for row in csv]
    uniqueGenres = list(set([elem.lower() for row in outputData for elem in row]))
    # remove invalid genres
    whitelist = [genre.lower() for genre in getWhitelist()]
    filteredGenres = filter(lambda x: x in whitelist, uniqueGenres)
    print filteredGenres
    # construct vector from output data
    
if __name__ == "__main__":
    handleCsv()
