# dialogue-condenser
A Python script that takes video (subtitled files) and outputs audio file(s) with intervals of silence removed. Utilizes the ffmpeg-python and moviepy libraries.

It can read and write the most common video/audio files, separately or in batches. The codecs that you can use to export with is based off your installation of ffmpeg-python (ffmpeg). By default, the program exports .mp3 audio-files. It has only been tested on Windows 10.

## How it works
This script works by reading subtitle file timestamps to detect when no dialogue occurs. Whenever there is a certain interval of silence, the program cuts out that portion of audio. Fade-in/out effects are applied in-between audio segments in order to improve the listening experience.

Accurate subtitle timing is preferable. However, padding is added to the beginning and end of audio segments (subclips) by default; the amount of padding can be configured in the settings file (settings.conf).
