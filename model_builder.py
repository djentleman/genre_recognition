# main.py, ties all the other files together

import scanner
import csv_interpreter as interpreter




def main():
    scanPath = r"C:/Users/Todd/Documents"
    csvPath = "csv.csv"
    scanner.clear(csvPath)
    # compile csv file
    scanner.processDirectory(scanPath, csvPath)
    # build vectors for theano
    metadataVector, inputVector, outputVector = interpreter.handleCsv(csvPath)
    # train deep neural net based on input and output vectors
    # save the model

if __name__ == "__main__":
    main()
