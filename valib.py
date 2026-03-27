from gtts import gTTS
from pygame import mixer
import os

talk_filename = "/mnt/ramdisk/talk.mp3"


def talk(text):
    tts = gTTS(text=text, lang='fr-ca')
    tts.save(talk_filename)
    mixer.init()
    mixer.music.load(talk_filename)
    mixer.music.play()
    while mixer.music.get_busy():
        pass
    os.remove(talk_filename)
