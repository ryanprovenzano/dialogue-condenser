import process
import os

fnames = os.listdir("./task") #Create list of mediafiles to run script on

file_suffix = "TRIM_" #Default prefix to put at beginning of output filename

with open("settings.conf") as f:
    for line in f:
        if "file_suffix" in line:
            pos = line.find("=")
            conf_value = line[pos+1:].strip()
            if conf_value == "default":
                break
            file_suffix = conf_value




for fname in fnames:
    split_name = fname.split('.')
    output_name = file_suffix + split_name[0] + ".mp3"
    process.run_xtract(fname, output_name)
