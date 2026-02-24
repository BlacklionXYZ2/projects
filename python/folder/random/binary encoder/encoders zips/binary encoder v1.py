
alph = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g': 7, 'h': 8, 'i': 9, 'j': 10, 'k': 11, 'l': 12, 'm': 13, 'n': 14, 'o': 15, 'p': 16, 'q': 17, 'r': 18, 's': 19, 't': 20, 'u': 21, 'v': 22, 'w': 23, 'x': 24, 'y': 25, 'z': 26, ' ': 27, '\n': 28, 
        '1': 29, '2': 30, '3': 31, '4': 32, '5': 33, '6': 34, '7': 35, '8': 36, '9': 37, '0': 38, '!': 39, '(': 40, ')': 41, '{': 42, '}': 43, '[': 44, ']': 45, '+': 46, '-': 47, '*': 48, '/': 49, '<': 50, '>': 51, '.': 52, ',': 53, "'": 54, '=': 55, ':': 56, '"': 57}

upper = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10, 'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15, 'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20, 'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26}

response = input('File name ')

class pFile:
    n = None
    e = None
    file = None
def parse(file):
    q = 0
    for x in file:
        if x != '.':
            q += 1
        else:
            pFile.n = file[0:q]
            pFile.e = file[q]
            pFile.file = pFile.n+pFile.e
            

parse(response)

response = input('Encode or decode ')

if response == 'encode':
    text = []
    binary = []

    def encode():
        binCode = 'a'
        f = open(pFile.file)
        for x in f.read():
            text.append(x)
        f.close()

        for x in text:
            if x in alph:
                binary.append('0'+f'{alph[x]:06b}')
            elif x in upper:
                binary.append('1'+f'{upper[x]:06b}')

        for x in binary:
            binCode += x
        binCode = binCode[1]

        f = open(f'encoded-{pFile.n}.txt', 'w')
        f.write(binCode)
        f.close()

    encode()

elif response == 'decode':
    def decode():
        f = open(f'encoded-{pFile.n}.txt')
        text = []
        
        i = 0
        a = 'a'
        binCode = None

        for x in f.read():
            i += 1
            a = a+x

            if i == 7:
                i = 0
                binCode = int(a[2], 2)
                isUpper = a[1]
                a = 'a'

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
        f = open(f'{pFile.n}.txt', 'w')
        for x in text:
            f.write(x)
        f.close()

    decode()