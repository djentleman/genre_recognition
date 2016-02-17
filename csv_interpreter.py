# interpreter for csv file

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
    
if __name__ == "__main__":
    handleCsv()
