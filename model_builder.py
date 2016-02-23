# main.py, ties all the other files together

import scanner
import csv_interpreter as interpreter
import utils.classification as classification



def main(*args):
    # I fucking love Python
    try:
        fullPipeline(args[0], args[1], args[2])
    except():
        test()


def constructNewCsv(scanPath, csvPath):
    # clean out oldCsv
    scanner.clear(csvPath)
    # compile csv file
    scanner.processDirectory(scanPath, csvPath)

def addToCsv(scanPath, csvPath):
    # compile csv file
    scanner.processDirectory(scanPath, csvPath)

def buildModel(csvPath, modelPath):
    metadataVector, inputVector, outputVector, genreVector = interpreter.handleCsv(csvPath)
    # train deep neural net based on input and output vectors
    cTools = classification.ClassificationTools(inputVector, outputVector)
    cTools.trainMultilayerPerceptron(learningRate=0.000001) 
    # save the model
    cTools.serializeModel(modelPath)

def fullPipeline(scanPath, csvPath, modelPath):
    constructNewCsv(scanPath, csvPath) 
    buildModel(csvPath, modelPath)

def test():
    scanPath = r"/root/music"
    csvPath = "csv.csv"
    #csvPath = "test.csv"
    modelPath = "model.dat"
    fullPipeline(scanPath, csvPath, modelPath)
    buildModel(csvPath, modelPath)

if __name__ == "__main__":
    #main(*args)
    test()
