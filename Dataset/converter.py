# COnvert mp3 file to wav file (vice versa)
import os
from glob import glob

import pydub

song_dir = 'C:\\Users\\asus\\Desktop\\Features\\*.mp3'  # Directory of File (Extension is acc. to initial file type, which we will convert)
# for converting mp3 to wav, put .mp3 here
print(song_dir)
song = glob(song_dir)  # Glob for pattern
print(song)
for song in song:
    mp3_song = os.path.splitext(song)[0] + '.wav'  # Changing the extension to the target file type
    sound = pydub.AudioSegment.from_mp3(song)
    sound.export(mp3_song, format="wav")  # COnversion using PyDub
    os.remove(song) # Remove this statement, to keep the original file
print("Conversion Done")
