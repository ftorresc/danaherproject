import pyttsx3
import keyboard

def onStart():
    if keyboard.is_pressed("esc"):
        print("Key pressed")
        engine.stop()

engine = pyttsx3.init()
engine.connect('started-word', onStart)
engine.say('The quick brown fox jumps over the lazy dog. The quick brown fox jumps over the lazy dog.')
engine.runAndWait()