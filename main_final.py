import os
import pickle
from tkinter import *
from tkinter import filedialog
#import tkFileDialog
#from FileDialog import askopenfilename
import tkinter as tk
from PIL import Image, ImageTk
import pygame
import pyaudio
import wave
import sys
import threading
from itertools import count
disp = ""
class ImageLabel(tk.Label):
    """a label that displays images, and plays them if they are gifs"""
    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)
        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)



def upload_file():

    fil = filedialog.askopenfilename()
    print (fil)
    pickle.dump( fil, open( "name.p", "wb" ), protocol = 2 )
    os.system('python2 test.py')
    disp = pickle.load(open( "disp.p", "rb" ))
    print(disp)
    data4.config(text = disp, width = 60)
    return fil
    '''
    file = tkFileDialog.askopenfile(parent=root,mode='rb',title='Choose a file')
    if file != None:
        data = file.read()
        print data
        file.close()
        print ("I got %d bytes from this file." % len(data))
    '''

def play_audio():
    global is_playing
    chunk = 1024
    file = upload_file()
    pygame.mixer.init()
    pygame.mixer.music.load(file)
    pygame.mixer.music.play()

    while pygame.mixer.music.get_busy() and is_playing: # is_playing to stop playing
        pass

    pygame.mixer.music.stop()


def press_button_play():
    global is_playing
    global my_thread

    if not is_playing:
        is_playing = True
        my_thread = threading.Thread(target=play_audio)
        my_thread.start()

def press_button_stop():
    global is_playing
    global my_thread

    if is_playing:
        is_playing = False
        my_thread.join()



def move_window(event):
    root.geometry('+{1}+{1}'.format(event.x_root, event.y_root))


root = tk.Tk()
lbl = ImageLabel(root)
lbl.place(x=0, y=0, relwidth=1, relheight=1)
lbl.load('small_BH.gif')
ws = root.winfo_screenwidth() # width of the screen
hs = root.winfo_screenheight() # height of the screen

w=800
h=600
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.overrideredirect(True) # turns off title bar, geometry
root.geometry('%dx%d+%d+%d' % (w, h, x, y)) # set new geometry

'''
frames = [PhotoImage(file='giphy.gif',format = 'gif -index %i' %(i)) for i in range(3)]

def update(ind):

    frame = frames[ind]
    ind = (ind+1)%3
    label.configure(image=frame)
    root.after(1000, update, ind)


#background image
image = Image.open('giphy.gif')
image=image.resize((850,650),Image.ANTIALIAS)
photo_image = ImageTk.PhotoImage(image)
label = tk.Label(root)
label.place(x=0, y=0, relwidth=1, relheight=1)
root.after(0, update, 0)
'''

# make a frame for the title bar
title_bar = Frame(root, bg='black', relief='raised', bd=2)

# bind title bar motion to the move window function
title_bar.bind('<B1-Motion>', move_window)
one=Label(title_bar,text="DEPRESSION DETECTION",bg="black",fg="white")
one.config(font=(15))
one.pack(side=TOP,fill='x')

# put a close button on the title bar
close_button = Button(title_bar, text='X', command=root.destroy,height=1,width=2)

# pack the title bar and close button
title_bar.pack(side=TOP, fill=X)
close_button.pack(side=RIGHT)





#__main__
is_playing = False
my_thread = None
data3=tk.Label(root,text="\n\n",bg="black")
data3.pack()
data=tk.Label(root,text="Depression is a mental health disorder characterised by persistently depressed mood or loss of \n interest in activities, causing significant impairment in daily life.\n\n",bg="black",fg="cyan")
data.config(font=("open sans",10))
data.pack()
data1=tk.Label(root,text="PLEASE UPLOAD YOUR AUDIO CLIP.",bg="black",fg="orange",compound=CENTER)
data1.config(font=("open sans",12))
data1.pack()
data2=tk.Label(root,text="\n\n",bg="black",fg="white")
data2.pack()





#for input button
#audio_in=Button(root,text="INPUT AUDIO",fg="white",bg="black",command=upload_file)
#audio_in.pack()
button_start = Button(root, text="INPUT AUDIO and PLAY",fg="white",bg="black", command=press_button_play)
button_start.pack()
data3=tk.Label(root,text="\n\n\n\n\n\n\n\n",bg="black",fg="white")
data3.pack()
data4=tk.Label(root,text=disp,bg="black",fg="white")
data4.pack()
data5=tk.Label(root,text="\n\n\n\n\n\n\n\n\n",bg="black",fg="white")
data5.pack()
button_stop = Button(root, text="STOP/DISCARD", fg="white",bg="black",command=press_button_stop)
#data2=tk.Label(root,text="\n\n\n\n\n\n\n\n",bg="black",fg="white")
button_stop.pack()



root.mainloop()
