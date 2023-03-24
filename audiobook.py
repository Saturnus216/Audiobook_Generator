# Developed by Dino Ceric
# Date 2023-03-24

import os
cwd = os.getcwd()


import tkinter as tk
from tkinter import *
import PyPDF2
import pyttsx3
from tkinter import filedialog

engine = pyttsx3.init()
root = Tk() #creating GUI window
root.geometry('400x350') #geometry of window
root.title("Audiobook Generator") #title of window

Label(root, text="AUDIOBOOK",font="Arial 15",bg='green').pack() 
m=tk.IntVar()
f=tk.IntVar()
def browse():
    global pdfReader
    file= filedialog.askopenfilename(title="Select a PDF", filetype=(("PDF    Files","*.pdf"),("All Files","*.*")))
    pdfReader = PyPDF2.PdfReader(open(file, 'rb'))
    pathlabel.config(text=file) #configuring the pathlabel Label

def save():
    global speaker
    speaker = pyttsx3.init()

    for page_num in range(len(pdfReader.pages)):
        text =  pdfReader.pages[page_num].extract_text()
        speaker.say(text)
        speaker.runAndWait()
        speaker.stop()

    voices = speaker.getProperty('voices')
    if m.get() == 0:
        speaker.setProperty('voice', voices[0].id)
    elif f.get() == 1:
        speaker.setProperty('voice', voices[1].id)

    speaker.save_to_file(text, 'audio.mp3')
    speaker.stop()

    Label(root, text="The Audio File is Saved").pack()
    
rate = engine.getProperty('rate')   
engine.setProperty('rate', 150)     

pathlabel = Label(root)
pathlabel.pack()

Button(root,text="Browse a File",command=browse).pack()
Button(root,text="Create and Save the Audio File ",command=save).pack()

Checkbutton(root,text="Male Voice",onvalue=0,offvalue=10,variable=m).pack()
Checkbutton(root,text="Female Voice",onvalue=1,offvalue=10,variable=f).pack()
root.mainloop()