import pygame as py
import pygame.mixer as mix
from mutagen.mp3 import MP3
from mutagen.id3 import ID3, APIC
import os, time
from io import BytesIO 
from PIL import Image, ImageTk
from datetime import datetime as date

py.init()
mix.init()

screen_width, screen_height = 300, 400
screeen = py.display.set_mode((screen_width, screen_height))

folder = 'files'
path = f'D://oscars shit//files//code//python//music player//{folder}'
songs = []
index = 0
for x in os.listdir(path):
    songs.append(f'music player/{folder}/{x}')

songEnd = py.USEREVENT + 1
mix.music.set_endevent(songEnd)

class button:
    def __init__(self, x, y, width, height, colour, text = None):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.colour = colour
        self.text = text

class play_button(button):
    def __init__(self, x, y, width, height, colour = (255, 0, 0), text = '|>'):
        super().__init__()

    def toggle(self):
        if self.colour == (255, 0, 0):
            self.colour = (0, 255, 0)
            mix.music.play()
            self.text = '||'
        elif self.colour == (0, 255, 0):
            self.colour = (255, 0, 0)
            mix.music.pause()
            self.text = '|>'

class skip_reverse_button(button):
    def __init__(self, x, y, width, height, colour):
        super().__init__()
    
play_pause = play_button(150, 200, 20, 20)


def play_next():
    global currentlyPLaying, songEnd
    
