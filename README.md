# dialogue-condenser
A Python script that takes video (subtitled files) and outputs audio file(s) with intervals of silence removed. Utilizes the ffmpeg-python and moviepy libraries.

It can read and write the most common video/audio files, separately or in batches. The codecs that you can use to export with is based off your installation of ffmpeg-python (ffmpeg). By default, the program exports .mp3 audio-files. It has only been tested on Windows 10.

## How it works
This script works by reading subtitle file timestamps to detect when no dialogue occurs. Whenever there is a certain interval of silence, the program cuts out that portion of audio. Fade-in/out effects are applied in-between audio segments in order to improve the listening experience.

Accurate subtitle timing is preferable. However, padding is added to the beginning and end of audio segments (subclips) by default; the amount of padding can be configured in the settings file (settings.conf).

## Installation
The main two dependencies are ffmpeg-python and moviepy. Running pip with both will install all the dependencies (if you haven't installed Python yet, install Python). 

This program hasn't been tested for all recent versions of Python 3, but there should be no issues with any Python 3 version. The last test of this program was done with 3.9.7.

Clone the repository to get all the necessary files.

## Instructions

Go into the folder (that you got from cloning the repository) and find the Task folder. Delete the deletethis.txt file inside the folder (this is just a placeholder file).

Drag the media files you want to operate on into the Task folder. It can operate on one or multiple files. 

To start the program, double-click on the condenser.py file or run it in a shell/terminal(e.g. CMD for Windows). You'll be prompted to select which audiotrack you want to operate on when the program starts. Usually, you will just select the only track contained (the 0th track). However, when a media file contains multiple audiotracks to pick from, you will need to figure out which audiotrack contains the audio in the language you want (so try with the 0th, 1st, 2nd, and so on until you find the right track).

This is why when you run the program with multiple files inside the Task folder, make sure either: a) all the mediafiles have only one track or b) all the mediafiles were created/obtained from the same source (so they will have uniform audiotrack assignment).

The output files from the program will appear in the condenser folder.

## Custom Settings

By going into the settings.conf file, you can edit various aspects of the program output. Note: all the numbers in the options are given in milliseconds.

**FilePrefix** can be changed to prefix your output files with the text of your choice. The default is TRIM_.

**SubclipStartPadding** and **SubclipEndPadding** will lengthen the audio segments. The audio segments are just what the program detects to be dialogue, and is found from the subtitle timings.

**SubclipStartPadding** adds the audio that precedes the original start of a segment. For example, setting this option to 400 will add 400 milliseconds of audio.

**SubclipEndPadding** does the same, but instead adds the audio that came after the original segment.

**FadeOutDuration** and **FadeInDuration** work a little bit differently. They add fade-in and fade-out FX to the audio segment without changing the timing. This means it is possible to ruin the dialogue comprehensibility by setting these to absurdly large numbers.

As you can see in the original settings, there are three different section titles (or whatever you want to call them): **[DEFAULT]**, **[2500ms]**, and **[5000ms]**. **Do not** get rid of the **[DEFAULT]** title. 

Basically, whatever is immediately under the DEFAULT section (i.e. until another section title) gets applied unless it's overwritten.

When will it be overwritten, you ask?

When the options from the other sections kick in. 

That basically happens when the gap of silence between the last dialogue segment reaches a certain length.

For example, if the amount of silence was greater than 2500 ms, but less than 5000 ms, the settings in the 2500ms section will kick in and override any previous option values. If it was 5000 ms or greater, than that section will kick in and override the option values.

In other words, the program will try to apply the settings that belong to the selection with the largest specified ms value. If it can't (because the amount of silence is too short), it will try the next largest section.

This allows us to basically have custom fade-in amounts based on the amount of silence preceding any dialogue. This can be used to suggest a significant scene change (currently it's configured so that longer fadeins mean the scene from your media file has probably just changed)

If you want to add new sections or change them, just make a new line containing an amount of milliseconds  wrapped by []. [1500ms], [2000ms], and [3000ms] are all valid section titles. And then simply put the options underneath that title that you want to be applied.

## Bugs

This program hasn't been extensively tested. It works most of the time, but has some bugs in some cases that I haven't fully worked out (where things are breaking in very noticeable ways).








