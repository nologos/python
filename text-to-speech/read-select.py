import pyttsx3
import os

textToRead = os.popen('xsel').read()
engine = pyttsx3.init()
engine.setProperty("voice", "en-us")
engine.say(textToRead)
engine.runAndWait()
