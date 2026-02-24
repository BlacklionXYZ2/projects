
response = input('File name?')


num = 0
text = []
index = {}
indexSort = {}


def findLen():
    num = 0
    for x in index:
        if x > num:
            num = x


def move():
    value = {i for i in index if index[i] == num}
    indexSort[value] = num
    index.pop(value)


def run(file):

    f = open(file)

    for x in f:
        text.append(str(x))

    for x in text:
        try:
            index[x] += 1
        except ValueError:
            index[x] = 1

    for x in index:
        findLen()
        move()
        
    #finish crap later
    #currently takes input file, converts it into a char list, takes frequency and sorts descending
    #needs to encode into arbitrary binary e.g. 'waayyy' = {'w': 11, 'a': 01, 'y': 1} <-- pain in the ass to decode