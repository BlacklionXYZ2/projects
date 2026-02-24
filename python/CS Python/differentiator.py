response = input()
split_response = response.split()
store = []


class num:
    def __init__(self, coefficient, exponent, negative):
        self.negative = negative
        self.coefficient = coefficient
        self.exponent = exponent

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

for x in split_response:
    if x not in ['+', '-']:
        try:
            store.append(format(x, operator))
        except NameError:
            store.append(format(x, '+'))
    operator = x

def output_formatter(data):
    if data.negative:
        return f'-{data.coefficient}x^{data.exponent}'
    else:
        return f'{data.coefficient}x^{data.exponent}'
    
def is_negative(coefficient, exponent, negative):
    out = 'a'
    if negative:
        if x == 0:
            out += f'-{coefficient}x^{exponent} '
        else:
            out += f'- {coefficient}x^{exponent} '
    else:
        if x == 0:
            out += f'{coefficient}x^{exponent} '
        else:
            out += f'+ {coefficient}x^{exponent} '
    return out[1:]

for x in store:
    print(x.coefficient, x.negative, x.exponent)
    
def output_single(data):
    out = 'a'
    for x in range(0, len(data)):
        if data[x].coefficient == 1:
            if data[x].exponent == 1:
                if data[x].negative:
                    if x == 0:
                        out += '-x '
                    else:
                        out += '- x '
                else:
                    if x == 0:
                        out += 'x '
                    else:
                        out += '+ x '
            elif data[x].exponent == 0:
                if data[x].negative:
                    if x == 0:
                        out += f'-{data[x].coefficient} '
                    else:
                        out += f'- {data[x].coefficient} '
                else:
                    if x == 0:
                        out += f'{data[x].coefficient} '
                    else:
                        out += f'+ {data[x].coefficient} '
            else:
                if data[x].negative:
                    if x == 0:
                        out += f'-x^{data[x].exponent} '
                    else:
                        out += f'- x^{data[x].exponent} '
                else:
                    if x == 0:
                        out += f'x^{data[x].exponent} '
                    else:
                        out += f'+ x^{data[x].exponent} '
        else:
            if data[x].exponent == 1:
                if data[x].negative:
                    if x == 0:
                        out += f'-{data[x].coefficient}x '
                    else:
                        out += f'- {data[x].coefficient}x '
                else:
                    if x == 0:
                        out += f'{data[x].coefficient}x '
                    else:
                        out += f'+ {data[x].coefficient}x '
            elif data[x].exponent == 0:
                if data[x].negative:
                    if x == 0:
                        out += f'-{data[x].coefficient} '
                    else:
                        out += f'- {data[x].coefficient} '
                else:
                    if x == 0:
                        out += f'{data[x].coefficient} '
                    else:
                        out += f'+ {data[x].coefficient} '
            else:
                if data[x].negative:
                    if x == 0:
                        out += f'-{data[x].coefficient}x^{data[x].exponent} '
                    else:
                        out += f'- {data[x].coefficient}x^{data[x].exponent} '
                else:
                    if x == 0:
                        out += f'{data[x].coefficient}x^{data[x].exponent} '
                    else:
                        out += f'+ {data[x].coefficient}x^{data[x].exponent} '


    return out[1:]

def differentiate(data):
    data.coefficient = data.exponent if data.exponent != 0 else 1
    data.exponent -= 1
    #check_int(data)

def integrate(data):
    data.exponent += 1
    data.coefficient /= data.exponent if data.exponent != 0 else 1
    #check_int(data)

for x in store:
    differentiate(x)
print(output_single(store))

for x in store:
    integrate(x)
print(output_single(store))