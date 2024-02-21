from gtts import gTTS
import os
t="wellcome to my python class vaidehi"
output=gTTS(text=t,lang="en",slow=False)
output.save("output.mp3")
os.system("start output.mp3")