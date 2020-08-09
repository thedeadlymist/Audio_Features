# Only supports .wav files
import wave

with wave.open("C:\\Users\\asus\\Desktop\\Features\\Teri Mitti.wav") as file:   # Song Directory
    print(file.getparams())
    
# Example - _wave_params(nchannels=2, sampwidth=2, framerate=32000, nframes=10051200, comptype='NONE', compname='not compressed')
