# dialogue-condenser
A Python script that takes video file(s) with subtitles and outputs audio-only file(s) with gaps of silence removed. Utilizes the ffmpeg-python and moviepy libraries.

It can read and write the most common video/audio files, separately or in batches. The codecs that you can use to export with is based off your installation of ffmpeg-python. By default, this script exports .mp3 audio-files and should work for all default installations. It has only been tested on Windows 10.

## How it works
This script works by reading the timestamps attached to videos' subtitle files. The timestamps are used to decide the audio segments that will be joined together. Whenever there is a gap in the timestamps for a certain period of time, the audio during then is filtered out. Fade-in/out FX are applied in-between audio segments in order to improve the listening experience.

Accurate subtitle timing is preferable. However, there are options inside the script to correct for when they are consistently timed poorly (too late or too early), or to increase the margin of error.

## Instructions
