import pyttsx3
import keyboard

def onStart():
    if keyboard.is_pressed("esc"):
        print("THE KEY HAS BEEN PRESSED OKAY")
        engine.stop()

engine = pyttsx3.init()
engine.connect('started-word', onStart)
engine.say('The quick brown fox jumped over the lazy dog in a devilish night of summer and fire.')
engine.runAndWait()