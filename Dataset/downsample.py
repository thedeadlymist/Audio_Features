'''
TODO

Rename File Properly
Check if Directory exists
Check th change in file size
'''

import os
import soundfile
from glob import glob
import librosa as lr

data_dir = 'C:\\Users\\asus\\Desktop\\Features\\Song\\*.wav'

audio_files = glob(data_dir)
len(audio_files)


for file in range(0, len(audio_files), 1):
    audio, sfreq = lr.load(audio_files[file], sr=16000, mono=True)
    soundfile.write('C:\\Users\\asus\\Desktop\\Features\\Song1\\%s.wav' % str(file+1).zfill(3), audio, 16000, subtype='PCM_24') # Song1 should exist beforehand
    print ('Done {}'.format(str(file)))
