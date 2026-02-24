from tkinter import ttk
from tkinter import *
import os 
import re

root = Tk()
access = []
accessTrue = {}
end = False
lastFile = 'a'

alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '\n': 28, 
        '1': 29, '2': 30, '3': 31, '4': 32, '5': 33, '6': 34, '7': 35, '8': 36, '9': 37, '0': 38, '!': 39, '(': 40, ')': 41, '{': 42, '}': 43, '[': 44, ']': 45, '+': 46, '-': 47, '*': 48, '/': 49, '<': 50, '>': 51, '.': 52, ',': 53, "'": 54, '=': 55, ':': 56, '"': 57}

upper = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}


class pFile:
    n = None
    e = None
    file = None
    eFile = None
def parse(file):
    q = 0

    for x in file:
        if x != '.':
            q += 1
        else:
            pFile.n = file[0:q]
            pFile.e = file[q:]
            pFile.file = pFile.n + pFile.e

    try:
        b = len(re.search('^encoded-b-', pFile.n))
    except TypeError:
        b = 0
    try:
        h = len(re.search('encoded-h-', pFile.n))
    except TypeError:
        h = 0

    print(b)

    if b > 0 or h > 0:
        pFile.n = pFile.n[11:]
    elif b > 0 and h > 0:
        pFile.n = pFile.n[22:]


text = []
binary = []

def encode():
    parse(str(drop.get()))
    access.append(pFile.file)
    end = False
    global lastFile

    if lastFile != pFile.file:
        lastFile = pFile.file
    else:
        try:
            if accessTrue[pFile.file] == True:
                root.destroy()
                end = True
        except KeyError:
            accessTrue[pFile.file] = True


    if end == False:
        binCode = 'a'

        f = open(f'folder//random crap//binary encoder//{pFile.file}')

        for x in f.read():
            text.append(x)
        f.close()

        for x in text:
            if x in alph:
                binary.append('00'+f'{alph[x]:06b}')
            elif x in upper:
                binary.append('01'+f'{upper[x]:06b}')

        for x in binary:
            binCode += x
        binCode = binCode[1:]

        f = open(f'folder//random crap//binary encoder//encoded-b-{pFile.n}.txt', 'w')
        f.write(binCode)
        f.close()


def decode():
    parse(str(drop.get()))
    access.append(pFile.eFile)
    end = False
    global lastFile

    if lastFile != pFile.file:
        lastFile = pFile.file
    else:
        try:
            if accessTrue[pFile.file] == True:
                root.destroy()
                end = True
        except KeyError:
            accessTrue[pFile.file] = True


    if end == False:
        f = open(f'folder//random crap//binary encoder//{pFile.file}')
        text = []
            
        i = 0
        a = 'a0'
        binCode = None

        for x in f.read():
            i += 1
            a = a+x

            if i == 8:
                i = 0
                binCode = int(a[3:], 2)
                isUpper = a[2]
                a = 'a0'

                if isUpper == '0':
                    for x in enumerate(alph):
                        t = list(x)

                        if t[0] + 1 == binCode:
                            text.append(t[1])

                elif isUpper == '1':
                    for x in enumerate(upper):
                        t = list(x)

                        if t[0] + 1 == binCode:
                            text.append(t[1])

            f.close()
            f = open(f'folder//random crap//binary encoder//{pFile.n}.txt', 'w')
            for x in text:
                f.write(x)
            f.close()


root.geometry('195x55')
root.minsize(195, 55)
root.maxsize(195, 55)

path = "C://Users//Oscar//Desktop//files//code//python//folder//random crap//binary encoder"
drop = ttk.Combobox(values = os.listdir(path))
drop.grid(row = 0, column = 0)
def refresh():
    drop.configure(values = os.listdir(path))
    print('run')
Button(root, text = 'Refresh', command = refresh).grid(row = 0, column = 1)

Button(root,text = 'Decode', command = decode).grid(row = 1, column = 0)
Button(root,text = 'Encode', command = encode).grid(row = 1, column = 1)

root.mainloop()