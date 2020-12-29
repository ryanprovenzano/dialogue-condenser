import os

import ffmpeg
from moviepy.editor import *

import loadsettings


#Functions to perform operations on timestamps
def get_timeinsecs(timestamp):
    unconverted_time = [int(timestamp[:2]), int(timestamp[3:5]), int(timestamp[6:8]), int(timestamp[9:12])]
    timeinsecs = (unconverted_time[0]*3600) + (unconverted_time[1]*60) + unconverted_time[2] + (unconverted_time[3]/1000)
    return timeinsecs

def update_times(start_time, end_time):
    a = get_timeinsecs(start_time)
    b = get_timeinsecs(end_time)
    return [a,b]


#Defining the main process of the program.

def run_xtract(fname, oname):

    #Selecting the audiotrack we want to extract
    while True:
        try:
            desired_audiotrack = int(input("Enter desired audiotrack (usually 0): "))
            break
        except:
            print("ERROR: Enter the audiotrack number in numeral form (1, 2, 3, 4, etc.)\n")

    #Extract subtitle from the mediafile
    (
        ffmpeg
        .input('./task/' + fname)
        .output("temp.srt")
        .run(overwrite_output = True)
    )
    #Exporting audio from the media when our desired audiotrack is not the first
    if desired_audiotrack != 0:
        in1 = ffmpeg.input('./task/' + fname)
        temp_ffmpeg_filename = "temp_" + fname
        out = ffmpeg.output(in1, temp_ffmpeg_filename, codec = "copy", map =f"0:a:{desired_audiotrack}")
        out.run(overwrite_output = True)


    #Load in video file; The file we load from depends on which audiotrack was selected by the user
    if desired_audiotrack == 0:             #
        audio_clip = (AudioFileClip('./task/' + fname))
    else:
        audio_clip = (AudioFileClip(temp_ffmpeg_filename))

    #Read timestamps from file and prepare subclip start/end times
    with open("temp.srt") as fhandle:

        subclip_store = list()

        current_times = [None, None]

        for line in fhandle:
            #check if it's the line we want
            if len(line)<6 or line[2] != ':':
                continue
            words = line.split()

            new_start_time, new_end_time = update_times(words[0], words[2])


            if current_times[0] is None:
                current_times = [new_start_time, new_end_time]
                continue

            if (new_start_time - current_times[1] < (loadsettings.interval_list_min / 1000)):
                current_times[1] = new_end_time

            else:
                for i in range(len(loadsettings.interval_list)):

                    if new_start_time - current_times[1] > loadsettings.interval_list[i] / 1000:

                        current_section_key = loadsettings.revert_to_string(loadsettings.interval_list[i])
                        current_interval = loadsettings.config[current_section_key]

                        current_times[0] = current_times[0] - (current_interval.getint('SubclipStartPadding') / 1000)
                        current_times[1] = current_times[1] + (current_interval.getint('SubclipEndPadding') / 1000)

                        editedclip = (audio_clip.subclip(current_times[0],current_times[1])
                                .audio_fadein(current_interval.getint('FadeInDuration') / 1000)
                                .audio_fadeout(current_interval.getint('FadeOutDuration') / 1000))
                        subclip_store.append(editedclip)
                        current_times = [new_start_time, new_end_time] #Prepare for next loop
                        break

        # Preparation of subclips complete
    print(subclip_store)
    concat = concatenate_audioclips(subclip_store)
    concat.write_audiofile(oname)
    audio_clip.close()

    #Delete temp files
    os.remove("temp.srt")
    if desired_audiotrack != 0:
        os.remove(temp_ffmpeg_filename)
