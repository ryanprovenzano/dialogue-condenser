import process
import os

fnames = os.listdir("./task") #Create list of mediafiles to run script on

file_suffix = "TRIM_" #Prefix to put at beginning of output filename



for fname in fnames:
    split_name = fname.split('.')
    output_name = file_suffix + split_name[0] + ".mp3"
    process.run_xtract(fname, output_name)
