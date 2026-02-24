import pygame as py
import pygame.mixer as mix
import tkinter as tk
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
import os, time
from io import BytesIO
from PIL import Image, ImageTk
from datetime import datetime as date

py.init()
mix.init()
root = tk.Tk()

folder = 'files'
path = f'python//music player//{folder}'
songs = []
index = 0
cover = tk.Label(root)
cover.pack()
title = tk.Label(root)
songTime = tk.Label()
class time:
    current = 0
    elapsedMins = 0

for x in os.listdir(path):
    songs.append(f'python/music player/{folder}/{x}')

songEnd = py.USEREVENT + 1
mix.music.set_endevent(songEnd)

def playNext():
    global index, startTime, currentlyPLaying, songLength
    startTime = date.now()
    if index < len(songs):
        mix.music.load(songs[index])
        mix.music.play()
        print(f'playing - {songs[index]}')

        currentlyPlaying = MP3(songs[index], ID3 = ID3)

        titleText = currentlyPlaying.tags.get('TIT2')
        if title:
            title.config(text = titleText.text[0])
        else:
            title.config(text = 'Unknown Title')

        for x in currentlyPlaying.tags.values():
            if isinstance(x, APIC):
                image = x.data
                run = True
                break
            else:
                run = False

        songLength = currentlyPlaying.info.length
        # startTime = time.time()
        index += 1
    else:
        index = 0
        playNext()

    if run:
        im = Image.open(BytesIO(image))
        im = im.resize((150, 150))
        currentImage = ImageTk.PhotoImage(image = im)
        cover.config(image = currentImage)
        cover.image = currentImage
 
def skip():
    playNext()

def previous():
    global index
    index -= 2
    playNext()

def pause():
    global paused
    if paused:
        mix.music.unpause()
        paused = False
    elif paused == False:
        mix.music.pause()
        paused = True
    else:
        print("something's wrong with the pause button")

def fmtTime(t):
    mins = int(t // 60)
    secs = int(t % 60)
    print(f'{mins}:{secs:02d}')
    return f'{mins}:{secs:02d}'

root.geometry('300x400')
root.minsize(300, 400)
root.maxsize(300, 400)

btnFrame = tk.Frame(root)
btnFrame.pack()

paused = False
playNext()

tk.Button(btnFrame, text = '<<', command = previous).grid(row = 1, column = 0, padx = 5)
tk.Button(btnFrame, text = '>>', command = skip).grid(row = 1, column = 2, padx = 5)
tk.Button(btnFrame, text = '^', command = pause).grid(row = 1, column = 1, padx = 5)

root.mainloop()