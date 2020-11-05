import process
import os

fnames = os.listdir("./task") #Create list of files in "Task" directory

fileSuffix = "TRIM_" #Suffix to put at beginning of output names



for fname in fnames:
    splitName = fname.split('.')
    outputName = fileSuffix + splitName[0] + ".mp3"
    process.run_xtract(fname, outputName)
