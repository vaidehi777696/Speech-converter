from gtts import gTTS
import os
from tkinter import *

root=Tk()
c1=Canvas(root,height=300,width=400)
c1.pack()
def texttospeech():
    t=entry.get()
    language='en'
    output=gTTS(text=t,lang='en',slow=False)
    output.save('output.mp3')
    os.system('start output.mp3')

text=Label(text="Text to speech convert APP",font=30,fg='red')
c1.create_window(200,100,window=text)
entry=Entry(root)
c1.create_window(200,180,window=entry)
button=Button(text='Converter',command=texttospeech)
c1.create_window(200,230,window=button)
root.mainloop()
