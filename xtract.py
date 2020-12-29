import os

import process_v2
import loadsettings

filenames = os.listdir("./task") #Create list of mediafiles to run through

def strip_filename_extension(string):
    temp = string.split('.')
    return temp[0]

for filename in filenames:
    stripped_filename = strip_filename_extension(filename)
    output_name = loadsettings.file_suffix + stripped_filename + ".mp3"
    process_v2.run_xtract(filename, output_name)
