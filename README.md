# subtitle-audio_condensor
A Python script that takes a video file with subtitles and produces, as a result, an audio-only file with moments lacking in speech removed. Utilizes the ffmpeg-python and moviepy libraries.

It can read and write the most common video/audio files, separately or in batches. The codecs that you can use to export with is based off your installation of ffmpeg-python. By default, this script exports .mp3 audio-files and should work for all users. It has only been tested on Windows, however, it should work for other platforms. 

## How it works
This script works by reading the timestamps attached to videos' subtitle files. Audio segments are then defined based off those timestamps. Essentially, when a lack of timestamps is detected for a predefined period of time, the audio during then is trimmed out. Fade-in and fade-out is applied in between each audio segment in order to improve the listening experience. 

Accurate subtitle timing is preferrable. However, I have provided a way to correct for when they are consistently timed poorly (for example, when the timestamps are consistently too late).

## Instructions



