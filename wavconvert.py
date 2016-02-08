# library for landing wav conversions and storage
import shutil # for now store the wav file on disk
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
    if fileFormat == "wav":
        moveWav(path, "tmp.wav")
    elif fileFromat == "mp3":
        convertFromMp3(path, "tmp.wav")
    elif fileFromat == "ogg":
        convertFromOgg(path, "tmp.wav")
    elif fileFromat == "flv":
        convertFromFlv(path, "tmp.wav")
        

def handleFile(path):
    if canConvert(path):
        convert(path)
    # now we can process tmp.wav
    
        
    
