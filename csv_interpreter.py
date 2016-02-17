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
             'chillout', 'techno', 'vaporwave',
             'trip-hop', 'downtempo', 'psychedelic',
             'breakcore', 'metal', 'best track ever',
             'idm', 'trap', 'rock', 'Acid', 'experimental']

def readCsv(path):
    return [row.split(",") for row in open(path, 'r').read().split("\n")]

def getPosition(elem, arr):
    try:
        return arr.index(elem)
    except:
        return -1

def handleCsv(path = "csv.csv"):
    # load csv into array
    csv = readCsv(path)
    # remove invalid records
    csv = filter(lambda x: len(x) > 2495, csv)
    # get vectors from csv
    metadataVector = [row[:3] for row in csv]
    inputVector = [row[3:2495] for row in csv]
    outputData = [row[2495:] for row in csv]
    # reformat output vector
    uniqueGenres = list(set([elem.lower() for row in outputData for elem in row]))
    # remove invalid genres
    whitelist = [genre.lower() for genre in getWhitelist()]
    filteredGenres = filter(lambda x: x in whitelist, uniqueGenres)
    # construct vector from output data
    outputVector = [[0]*len(filteredGenres) for row in outputData]
    for i in range(len(outputData)):
        outputLine = outputData[i]
        for genre in outputLine:
            pos = getPosition(genre.lower(), filteredGenres)
            if pos != -1:
                outputVector[i][pos] = 1
    #now we have out vectors, we can hand things over to theano
    return metadataVector, inputVector, outputVector
            
    
    
if __name__ == "__main__":
    handleCsv()
