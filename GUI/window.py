import os
import tkinter.messagebox
from tkinter import *
from tkinter import filedialog
from pygame import mixer

root = Tk()
mixer.init()

# Creating a menubar ...
menubar = Menu(root)
root.config(menu=menubar)

# Creating a submenu ...
subMenu = Menu(menubar, tearoff=0)


def browse_file():
    global filename
    filename = filedialog.askopenfilename()
    # print(filename)


subMenu.add_command(label='Open', command=browse_file)
subMenu.add_command(label='Exit', command=root.destroy)
menubar.add_cascade(label='File', menu=subMenu)
subMenu.add_separator()


def about_us():
    tkinter.messagebox.showinfo('Melody Player', 'This is the Melody player built using Python')


Help = Menu(menubar, tearoff=0)
Help.add_command(label="About Us", command=about_us)
menubar.add_cascade(label="Help", menu=Help)

root.title("Melody")
root.geometry("350x350")
root.iconbitmap(r'music.ico')

text = Label(root, text='Lets make some noise!!!!')
text.pack()


def play_music():
    try:
        paused
    except NameError:
        try:
            mixer.music.load('music.mp3')  # we can use filename variable....
            mixer.music.play()
            statusBar['text'] = "Playing Music" + ' - ' + os.path.basename('music.mp3')
        except:
            tkinter.messagebox.showerror('File Not Found', 'Could not found a file, please select a file to play!!!!')
    else:
        mixer.music.unpause()
        statusBar['text'] = "Music Resumed"


# mixer.music.pause()

def pause_music():
    global paused
    paused = TRUE
    mixer.music.pause()
    statusBar['text'] = "Music Paused"


def stop_music():
    mixer.music.stop()
    statusBar['text'] = "Stopped Music"


def set_vol(val):
    volume = int(val) / 100
    mixer.music.set_volume(volume)  # set_volume takes either zero or one as its values in tha range (0,0.1,..0.99,1)


playPhoto = PhotoImage(file='Play.png')
playBtn = Button(root, image=playPhoto, command=play_music)
playBtn.pack()

pausePhoto = PhotoImage(file='pause.png')
pauseBtn = Button(root, image=pausePhoto, command=pause_music)
pauseBtn.pack()

stopPhoto = PhotoImage(file='stop2.png')
stopbtn = Button(root, image=stopPhoto, command=stop_music)
stopbtn.pack()

scale = Scale(root, from_=0, to=100, orient=HORIZONTAL, command=set_vol)
scale.set(55)
mixer.music.set_volume(0.55)
scale.pack()

statusBar = Label(root, text="Welcome to Melody!!", relief=SUNKEN, anchor=W)
statusBar.pack(side=BOTTOM, fill=X)

root.mainloop()
