from gtts import gTTS
import os

try:
    #a = input("What you want me to say: ")
    #a = unicode(a, "utf-8")
    tts = gTTS(text=(os.popen('xsel').read()), lang="en")
    
    testfile = "/tmp/temp.mp3"
    tts.save(testfile)

    os.system("cvlc --play-and-exit --rate 1.7 /tmp/temp.mp3")
    print("\033[H\033[J")
    os.unlink(testfile)
except UnicodeDecodeError:
    print("Some characters are not supported.")




#selected_text=(os.popen('xsel').read())
