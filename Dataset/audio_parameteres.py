# Only supports .wav files
import wave

with wave.open("C:\\Users\\asus\\Desktop\\Features\\Teri Mitti.wav") as file:   # Song Directory
    print(file.getparams())
