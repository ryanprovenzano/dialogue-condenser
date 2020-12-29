import os

import process_v2
import loadsettings

fnames = os.listdir("./task") #Create list of mediafiles to run through

def strip_filename_extension(string):
    temp = string.split('.')
    return temp[0]

for fname in fnames:
    fname = strip_filename_extension(fname)
    output_name = loadsettings.file_suffix + fname + ".mp3"
    process_v2.run_xtract(fname, output_name)
