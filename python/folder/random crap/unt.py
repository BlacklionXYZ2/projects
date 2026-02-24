
class sort:
    num = []
    string = []
    boolean = []
    other = []

data = [1234, 'deez', 1.111, True, [12, 3]]

def sort2(file):
    for x in file:

        if type(x) == bool:
            sort.boolean.append(x)

        elif type(x) == int or float:
            sort.num.append(x)

        elif type(x) == str:
            sort.string.append(x)

        else:
            sort.other.append(x)

    print(sort.num)
    


sort2(data)