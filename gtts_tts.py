#VSC_gtts example from programmingknowlege 2020-12-01
import os
from gtts import gTTS

myText = "Text To Speech Conversion"
language = 'en'

output = gTTS(text=myText, lang=language, slow=False)

output.save("output.mp3")

os.system("start output.mp3")