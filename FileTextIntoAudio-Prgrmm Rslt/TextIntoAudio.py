from  gtts import gTTS
# pip install gtts
from playsound import playsound
# pip install playsound

audio = 'speech.mp3'
language = 'en'
sp = gTTS(text = "enter your text to convert into audio", lang= language,slow=False)

sp.save(audio)
playsound(audio)