cars = [["Ford","Mondeo",123],[57,"Focus",bool(1)],[9.03,"Yaris","BAZ8447"]]
boolean = []
string = []
other = []
for x in cars:
    for y in x:
        if type(y) == bool:
            boolean.append(y)
        elif type(y) == str:
            string.append(y)
        else:
            other.append(tuple(y, type(y)))
print(boolean, string, other)