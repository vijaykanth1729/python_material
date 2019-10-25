from tkinter import *
from pygame import mixer


root = Tk()
mixer.init()

root.title('Gaming Console!')
root.geometry('700x700')
root.iconbitmap(r'game.ico')

menubar = Menu(root)
root.config(menu=menubar)

FileMenu = Menu(menubar,tearoff=0)
menubar.add_separator()
HelpMenu = Menu(menubar,tearoff=0)


FileMenu.add_command(label='Open')
FileMenu.add_command(label='close')
menubar.add_cascade(label='File', menu=FileMenu)



HelpMenu.add_command(label='Contact')
HelpMenu.add_command(label='TroubleShoot')
menubar.add_cascade(label='Help',menu=HelpMenu)




text = Label(root,text="This is a GAMING console!!")
text.pack()





def play_game():
    mixer.music.load('music.mp3')
    mixer.music.play()

game = PhotoImage(file='Play.png')

gamebtn = Button(root,image=game,command=play_game)
gamebtn.pack()

root.mainloop()