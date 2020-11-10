import os
import ffmpeg
from moviepy.editor import *


#Config

#Buffer between subclips, in milliseconds
subclip_buffer = 1500

#Buffer before subtitle time starts, in milliseconds
before_buffer = 250

#Buffer after subtitle time ends, in milliseconds
after_buffer = 250

#Fade after each subclip, in milliseconds
fadeout_duration = 250

#Fade in the beginning of a subclip, in milliseconds
fadein_duration = 50

#Extract subtitle & load videofile

temp = 'temp.srt'

#Process subtitle file

def get_timeinsecs(timestamp):
    unconverted_time = [int(timestamp[:2]), int(timestamp[3:5]), int(timestamp[6:8]), int(timestamp[9:12])]
    timeinsecs = (unconverted_time[0]*3600) + (unconverted_time[1]*60) + unconverted_time[2] + (unconverted_time[3]/1000)
    return timeinsecs

def update_times(start_time, end_time):
    a = get_timeinsecs(start_time)
    b = get_timeinsecs(end_time)
    return [a,b]


def run_xtract(fname, oname):

    desired_audiotrack = int(input("Enter desired audiotrack (usually 0): "))

    (
        ffmpeg
        .input('./task/' + fname)
        .output(temp)
        .run(overwrite_output = True)
    )

    if desired_audiotrack != 0:
        in1 = ffmpeg.input('./task/' + fname)
        temp_ffmpeg_filename = "temp_" + fname
        out = ffmpeg.output(in1, temp_ffmpeg_filename, codec = "copy", map =f"0:a:{desired_audiotrack}")
        out.run(overwrite_output = True)

    fhandle = open(temp)



    desired_subclip_times = list()

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

        if (new_start_time - current_times[1] < (subclip_buffer / 1000)):
            current_times[1] = new_end_time

        else:
            current_times[1] = current_times[1] + (after_buffer / 1000)
            current_times[0] = current_times[0] - (before_buffer / 1000)
            desired_subclip_times.append(current_times)
            current_times = [new_start_time, new_end_time]


    subclip_store = list()

    #Load, then edit audio

    if desired_audiotrack == 0:
        audio_clip = (AudioFileClip('./task/' + fname))
    else:
        audio_clip = (AudioFileClip(temp_ffmpeg_filename))

    for clip in desired_subclip_times:
        editedclip = (audio_clip.subclip(clip[0],clip[1])
                .audio_fadein(fadein_duration / 1000)
                .audio_fadeout(fadeout_duration / 1000))
        subclip_store.append(editedclip)

    concat = concatenate_audioclips(subclip_store)

    concat.write_audiofile(oname)


    fhandle.close()
    audio_clip.close()

    #Delete temp file
    os.remove(temp)
    if desired_audiotrack != 0:
        os.remove(temp_ffmpeg_filename)
