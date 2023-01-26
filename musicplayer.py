from pygame import mixer
from tkinter import Button
from tkinter import Tk
from tkinter import Label
from tkinter import filedialog
import os

current_volume =float(0.5)

#fonctions

def play_song():
    filename = filedialog.askopenfilename(initialdir="./playerMusic/Musique", title="Select a file")
    current_song = filename
    song_name = os.path.basename(filename)
    print(song_name)
    
    try: 
        mixer.init()
        mixer.music.load(current_song)
        mixer.music.set_volume(current_volume)
        mixer.music.play()
        song_title_label.config(fg="green", text="Now play: " + str(song_name))
        volume_label.config(fg="green", text="Volume : " +str(current_volume))
    except Exception as e :
        print(e)
        song_title_label.config(fg="red", text="Erreur en essayant de jouer ")
    
        
def increase_volume():
    try: 
        global current_volume
        if current_volume >= 1:
            volume_label.config(fg="green", text="Volume : Max")
            return
        current_volume = current_volume + float(0.1) 
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Musique pas encore séléctionnée !")
    
def reduce_volume():    
    try:
        global current_volume
        if current_volume <= 0:
            volume_label.config(fg="red", text="Volume : Eteint")
            return
        current_volume = current_volume - float(0.1) 
        current_volume = round(current_volume, 1)
        mixer.music.set_volume(current_volume)
        volume_label.config(fg="green", text="Volume : "+str(current_volume))
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Musique pas encore séléctionnée !")
        
def pause():
    try:
        mixer.music.pause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Musique non séléctionnée ")
def resume():
    try:
        mixer.music.unpause()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Musique non séléctionnée ")

def stop():
    try:
        mixer.music.stop()
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Musique non séléctionnée ")

def boucle():
    try:
        mixer.music.play(loop=-1)
    except Exception as e:
        print(e)
        song_title_label.config(fg="red", text="Musique non séléctionnée ")

def sauter(position):
    mixer.music.set_pos(position)
    
        

    
#Main screen
master = Tk()
master.title("Music Player")
master.geometry("800x250")
#Labels
Label(master,text='Custom Cez',font=("Calibri", 15), fg="blue").grid(sticky="N", row=0, padx=280)
Label(master,text='Volume',font=("Calibri", 12, 'bold'), fg="violet").grid(sticky="N", row=4)
song_title_label = Label(master, font=("Calibri",12))
song_title_label.grid(stick="N", row=3)
volume_label = Label(master, font=("Calibri",12))
volume_label.grid(stick="N", row=5)

#Bouttons
Button(master, text="Selectionner un son", font=("Calibri, 12"), command=play_song).grid(row=2, sticky="N")
Button(master, text="Pause", font=("Calibri, 12"), command=pause).grid(row=3, sticky="E", padx=10)
Button(master, text="Play", font=("Calibri, 12"), command=resume).grid(row=3, sticky="W")
Button(master, text="-", font=("Calibri, 12"), width=3, command=reduce_volume).grid(row=5, sticky="W")
Button(master, text="+", font=("Calibri, 12"), width=5, command=increase_volume).grid(row=5, sticky="E")
Button(master, text="Stop", font=("Calibri, 12"), width=4, command=stop).grid(row=4, sticky="E", padx=10)
Button(master, text="En Boucle", font=("Calibri, 12"), width=5, command=boucle).grid(row=4, sticky="W")
Button(master, text="Sauter", command=lambda: sauter(30)).grid(row=5, sticky="S", pady=40)

master.mainloop()