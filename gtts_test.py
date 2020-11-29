#VSC_gtts testas 2020-11-26 vscode done

from gtts import gTTS
from playsound import playsound

def play_audio(audio):
    playsound(audio)

def convert_to_audio(text):
    audio =gTTS(text)
    audio.save("textaudio.mp3")
    play_audio("textaudio.mp3")

convert_to_audio("laba diena dainiau")

