from gtts import gTTS
import os

try:
    tts = gTTS(text=(os.popen('xsel').read()), lang="en")           # GTTS - google speach api, os.popen - execute comand, xsel - return selected text
    
    testfile = "/tmp/temp.mp3"                                      # create a var filename
    tts.save(testfile)                                              # save GTTS to var

    os.system("cvlc --play-and-exit --rate 1.7 /tmp/temp.mp3")      # play in vlc hiden exit after 
    print("\033[H\033[J")                                           # cleasrs the screen
    os.unlink(testfile)                                             # better way to remove the file 
except UnicodeDecodeError:
    print("Some characters are not supported.")                     # error handling