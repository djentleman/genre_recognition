# directory scanner

import track
import os
from os.path import isfile, join


def processDirectory(path):
    tracks = []
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
            tracks.append(track.Track(path + "/" + fpath))
    for dpath in dirs:
        tracks += processDirectory(path + "/" + dpath)
    return tracks
        
    

if __name__ == "__main__":
    tracks = processDirectory(r"C:/Users/Todd/Documents")
    for sound in tracks: sound.dump()
    
