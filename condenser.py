import os

import package1.process as process
import package1.loadsettings as loadsettings

filenames = os.listdir("./task") #Create list of mediafiles to run through
if filenames == []:
    print( "\nERROR: Task folder is empty. Put in video file(s) that you want to condense." )
    quit()

def strip_filename_extension(string):
    temp = string.split('.')
    return temp[0]

for filename in filenames:
    stripped_filename = strip_filename_extension(filename)
    output_name = loadsettings.file_suffix + stripped_filename + ".mp3"
    process.run_condenser(filename, output_name)
