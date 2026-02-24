import re
import os
from tkinter import *
from tkinter import ttk

hexadecimal = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}

alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '\n': 28, 
        '1': 29, '2': 30, '3': 31, '4': 32, '5': 33, '6': 34, '7': 35, '8': 36, '9': 37, '0': 38, '!': 39, '(': 40, ')': 41, '{': 42, '}': 43, '[': 44, ']': 45, '+': 46, '-': 47, '*': 48, '/': 49, '<': 50, '>': 51, '.': 52, ',': 53, "'": 54, '=': 55, ':': 56, '"': 57}

upper = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}



root = Tk()
finalText = 'a'
text = 'a'
binary = 'a'
lastFile = 'a'
values = []
access = []
accessTrue = {}
end = False
l = 0

class pFile:
    n = None
    e = None
    file = None
    eFile = None

def valueReset():
    global finalText, text, binary, values, l
    finalText = 'a'
    text = 'a'
    binary = 'a'
    values = []
    l = 0

def parse(file):
    q = 0
    pFile.efile = file

    for x in file:
        if x != '.':
            q += 1
        else:
            pFile.n = file[0:q]
            pFile.e = file[q:]
            pFile.file = pFile.n + pFile.e
    
    try:
        b = len(re.search('encoded-b-', pFile.n))
    except TypeError:
        b = 0
    try:
        h = len(re.search('encoded-h-', pFile.n))
    except TypeError:
        h = 0
        
    if b > 0 or h > 0:
        pFile.n = pFile.n[11:]
    elif b > 0 and h > 0:
        pFile.n = pFile.n[22:]

def hexEncode():
    parse(str(drop.get()))
    access.append(pFile.file)
    end = False
    global lastFile, binary, text, hexadecimal
    text = 'a'

    f = open(f'folder//random crap//binary encoder//{pFile.file}')

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
        t = 0
        for x in f.read():
            t += 1
            binary = binary + x   #add binary characters until there are enough for a hex character
            if len(binary) - 1 == 4:
                #print('len 4')
                binary = binary[1:] #remove prefix/placeholder 'a'
                for value, key in enumerate(hexadecimal):  #compare the int value assigned to each hex char to each 4bit binary value
                    #print(list(y))
                    #print(binary)
                    if value == int(binary, 2): #check if the binary value and the hex value are equal
                        text += key #add the hex character to the output text
                        #print(text)
                        binary = 'a' #reset binary and end this loop
                        break
                t = 0

        f.close()
        f = open(f'folder//random crap//binary encoder//encoded-h-{pFile.n}.txt', 'w')
        #print('open')
        f.write(text[1:])
        #print('write')
        #print(text[1:])
        f.close()
        #print('close')
        valueReset()


def binConvert():
    global upper, alph, text, finalText, values

    #check if the character should be capital or not (the second bit defines this)
    for x in values:
        if x[1] == '1':
            capsTrue = True
        else: 
            capsTrue = False

        #convert 6 bit binary back into integer
        v = int(x[2:], 2)
        #print(capsTrue, x, v)

        #check the spcified dictionary for equal values and add the keys of the values to the final text
        if capsTrue:
            print('capsTrue')
            for value, key in enumerate(upper):
                print(v, key, value)
                if v == value:
                    finalText += key
                    print(key, value, finalText)
                    break

        elif capsTrue == False:
            print('capsFalse')
            for value, key in enumerate(alph):
                print(v, key, value)
                if v == value:
                    finalText += key
                    print(key, value, finalText)
                    break


def hexDecode():
    parse(str(drop.get()))
    access.append(pFile.file)
    global lastFile, binary, text, finalText, hexadecimal, upper, alph, l

    f = open(f'folder//random crap//binary encoder//{pFile.file}', 'r')

    #check if the last file encoded/decoded was this file
    if lastFile != pFile.file:
        lastFile = pFile.file
    else:
        try:
            if accessTrue[pFile.file] == True:
                root.destroy()
        except KeyError:
            accessTrue[pFile.file] = True

    #take all the characters in the read file and convert the into binary
    for x in f.read():
        #print(x)
        for key in enumerate(hexadecimal):
            key = list(key)
            #print(key, x)
            if x == key[1]:
                binary = f'{key[0]:04b}'
                text += binary
                #print(binary, 'binary')
                #print(text, 'text')

    #loop through text and split it into 8 character parts
    for x in text:
        if l == 7:
            values.append(text[0:l])
            text = text[l:]
            #print(l, text, values)
            l = 0
            #print(l)
        l += 1

    binConvert()
    #print(finalText)

    #closes the read file and creates the new text file with the decoded text
    f.close()
    #print(pFile.n)
    f = open(f'folder//random crap//binary encoder//{pFile.n}.txt', 'w')
    #print('open')
    #print(finalText[1:])
    f.write(finalText[1:]) # <- for some unknown reason finalText never has its value updated despite it being declared globally in both hexDecode() and binConvert()
    #print('write')
    #print('close')
    f.close()
    #print('end')
    valueReset()

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

Button(root,text = 'Decode', command = hexDecode).grid(row = 1, column = 0)
Button(root,text = 'Encode', command = hexEncode).grid(row = 1, column = 1)

root.mainloop()
