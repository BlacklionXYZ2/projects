
data = [123, [2, 4], 5]
save = []

cont = []


def checkDist(f):
    for x in f:
        if type(x) == list:
            cont.append(True)
        else:
            cont.append(False)

def loop(obj):
    checkDist(obj)
    x = 0
    while x < len(obj):
        
        if cont[x] == True:
            loop(obj[x])

        save.append(obj[x])


def start():
    save.clear()
    cont.clear()
    loop(data)
    print(save)

start()


            

        
        