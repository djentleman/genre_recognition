# library for landing wav conversions and storage
import shutil # for now store the wav file on disk
import os
from pydub import AudioSegment  # conversion to wav


def convertFromMp3(inpath, outpath):
    sound = AudioSegment.from_mp3(inpath)
    sound.export(outpath, format="wav")

def convertFromOgg(inpath, outpath):
    sound = AudioSegment.from_ogg(inpath)
    sound.export(outpath, format="wav")

def convertFromFlv(inpath, outpath):
    sound = AudioSegment.from_flv(inpath)
    sound.export(outpath, format="wav")

def moveWav(infile, outfile):
    shutil(infile, outfile)

def canConvert(path):
    fileFormat = path.split(".")[-1]
    return (fileFormat == "wav" or
            fileFormat == "mp3" or
            fileFormat == "ogg" or
            fileFormat == "flv")

def convert(path):
    fileFormat = path.split(".")[-1]
    outpath = "tmp.wav"
    if fileFormat == "wav":
        moveWav(path, outpath)
    elif fileFormat == "mp3":
        convertFromMp3(path, outpath)
    elif fileFormat == "ogg":
        convertFromOgg(path, outpath)
    elif fileFormat == "flv":
        convertFromFlv(path, outpath)
        

def convertFile(path):
    if canConvert(path):
        convert(path)
        return True
    return False
    # now we can process tmp.wav

def destroyTmp():
    path = "tmp.wav"
    os.remove(path)
    

if __name__ == "__main__":
    path = "C:\Users\Todd\Music\song.mp3"
    convertFile(path)
    destroyTmp()

        
    
