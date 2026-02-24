alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
response = input()
split_response = response.split()
store = []
charset = [char if char in alph else None for char in response]
print(charset)
remove = []
for x in range(len(charset)):
    if charset[x] == None:
        remove.append(x)
const = len(remove)
for x in range(len(charset)):
    print(charset)
    print(x, x - const + len(remove), remove)
    if x in remove:
        remove.remove(x)
        charset.pop(x - const + len(remove) + 1)
print(charset)



class num:
    def __init__(self, char, coefficient, exponent, negative):
        self.negative = negative
        self.coefficient = coefficient
        self.exponent = exponent
        self.char = char

def check_int(data):
    if int(data.coefficient) == data.coefficient:
        data.coefficient = int(data.coefficient)
    if int(data.exponent) == data.exponent:
        data.exponent = int(data.exponent)


def format(data, operator):
    coefficient_location = data.find('x')
    exponent_location = data.find('^')
    coefficient = None
    negative = None
    exponent = None

    if operator == '+':
        negative = False
    elif operator == '-':
        negative = True

    if coefficient_location not in [0, -1]:
        coefficient = round(float(eval(data[:coefficient_location])), 2)
    elif coefficient_location == -1:
        coefficient = float(data)
    else:
        coefficient = 1

    if exponent_location not in [0, -1]:
        exponent = round(float(eval(data[exponent_location + 1:])), 2)
    elif exponent_location == -1:
        exponent = 0
    else:
        exponent = 1

    if coefficient_location >= 0 and exponent_location == -1:
        exponent = 1

    temp = num(coefficient, exponent, negative)

    #check_int(temp)

    return temp