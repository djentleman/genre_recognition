# -*- coding: utf-8 -*-
# directory scanner

import utils.dataset as dataset
import utils.track as track
import os
from os.path import isfile, join

def clear(path):
    open(path, 'w').write('')

def processDirectory(path, csvPath):
    tracks = dataset.Dataset(csvPath)
    print path
    #print tracks
    try:
        ls = os.listdir(path)
    except:
        return tracks
    #print ls
    files = filter(lambda f: isfile(join(path, f)), ls)
    dirs = filter(lambda f: not isfile(join(path, f)), ls)
    for fpath in files:
        if track.isValidPath(path + "/" + fpath):
            tracks.addPath(path + "/" + fpath)
    for dpath in dirs:
        processDirectory(path + "/" + dpath, csvPath)
        

if __name__ == "__main__":
    processDirectory(r"C:/Users/Todd/Documents", "csv.csv")
    
    
