from tkinter import *
from pygame import mixer       #pip install pygame

root = Tk()

mixer.init()

root.title('Music-Player')
root.geometry('300x300')

text = Label(root, text="This is a music player")
text.pack()

photo = PhotoImage(file='Play.png')
photostop = PhotoImage(file='stop.png')


def play_music():
    mixer.music.load('music.mp3')
    mixer.music.play()


def stop_music():
    mixer.music.stop()

imagebtn = Button(root, image=photo,command=play_music)
imagebtn.pack()

imagebtn1 = Button(root, image=photostop,command=stop_music)
imagebtn1.pack()

root.mainloop()    #it maintains consstancy of a window..
