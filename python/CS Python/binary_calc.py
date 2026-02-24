response = input()
response = response.split()
nums = []
ops = []
binary = []
denary = [False]
negative = False

#binary 'formatter' (converts inputs into reversed lists (leftmost digit becomes rightmost for linear search operations))
def format(data):
    out = []
    negative = False
    if data[0] in ['0', '1', '-'] and len(data) > 1 or data in ['0', '1']:
        if data[0] == '-':
            negative = True
            for x in range(1, len(data)):
                out.append(data[len(data) - x])

        elif data[len(data) - 1] in [True, False]:
            for x in range(0, len(data) - 1):
                out.append(data[len(data) - x - 2])

        else:
            for x in range(0, len(data)):
                out.append(data[len(data) - x - 1])

        if negative:
            out.append(negative)
            negative = False
        else:
            out.append(negative)
            print(out)
        return out
    else:
        print([data])
        return [data]

for x in response:
    binary.append(format(x))

def strFormat(data):
    out = 'a'
    if type(data) == list:
        if type(data[len(data) - 1]) == bool:
            for x in range(0, len(data) - 2):
                print(x)
                out += data[len(data) - x - 2]
        else:
            for x in range(0, len(data) - 1):
                if x == len(data) - 1:
                    out += data[x]
                else:
                    out += data[x] + ', '
                if data[len(data[x]) - 1] == True: # fix to activate for each number in nums so they can be defined as negative or not
                    negative = True
        print(out)
        return out
    else:
        print(f'Unsupported Output Type: {type(data)}')
        
def binary_adder(num1, num2):
    out = []
    carry = False
    negative = False

    if len(num1) > len(num2):
        if num2[len(num2) - 1]:
            negative = True
        else:
            negative = False
            num2.pop(len(num2) - 1)
        for x in range(len(num2), len(num1) - 1):
            num2.append('0')
        if negative:
            num2.append(True)
        else:
            num2.append(False)
            
    elif len(num1) < len(num1):
        if num1[len(num1) - 1]:
            negative = True
        else:
            negative = False
            num1.pop(len(num1) - 1)
        for x in range(len(num1), len(num2) - 1):
            num1.append('0')
        if negative:
            num1.append(True)
        else:
            num1.append(False)

    print(num1, num2)

    for x in range(0, len(num1) - 1):
        if num1[x] == '0' and num2[x] == '0':
            if carry:
                out.append('1')
                carry = False
            else:
                out.append('0')
        elif num1[x] == '1' and num2[x] == '0':
            if carry:
                out.append('0')
            else:
                out.append('1')
        elif num1[x] == '0' and num2[x] == '1':
            if carry:
                out.append('0')
            else:
                out.append('1')
        elif num1[x] == '1' and num2[x] == '1':
            if carry:
                out.append('1')
                carry = False
            else:
                out.append('0')
                carry = True

    if carry:
        out.append('1')
        carry = False
    print(out)
  
    return out

def twosCompliment(num):
    flip = False
    for x in range(0, len(num) - 1):
        if num[x] == '1' and flip == False:
            flip = True
        elif flip == True:
            if num[x] == '0':
                num[x] = '1'
            elif num[x] == '1':
                num[x] = '0'


def add(num1, num2):
    return binary_adder(num1, num2)

def subtract(num1, num2):
    store_num1 = denaryConverter(format(num1))
    out = []

    twosCompliment(num2)
    num2[len(num2) - 1] = True

    out = add(num1, num2)

    if out[len(out) - 1] == '1':
        out[len(out) - 1] = '0'
    elif out[len(out) - 1] == '0':
        out[len(out) - 1] = '1'
    
    if denaryConverter(format(out)) > store_num1:
        if out[len(out) - 1] == '1':
            out[len(out) - 1] = '0'
        elif out[len(out) - 1] == '0':
            out[len(out) - 1] = '1'
        out.append(True)

    else:
        out.append(False)

    if not num1[len(num1) - 1]:
        twosCompliment(out)

    print(out)
    return out

def multiply(num, mult):
    out = num
    for x in range(0, int(mult, base = 2)):
        out = add(out, num)
    return out

def denaryConverter(data):
    out = 'a'
    for x in data:
        if x in [True, False]:
            pass
        else:
            out += x
    return int(out[1:], base = 2)


operations = ['add', '+', 'subtract', '-', '*', 'denary']

#action splitter (separates numbers and actions)
for x in binary:
    if x[0] in operations:
        ops.append(x[0])
    else:
        nums.append(x)

#action series
for x in ops:
    if x in ['add', '+']:
        nums[0] = add(nums[0], nums[1])
        nums.pop(1)
    elif x in ['subtract', '-']:
        nums[0] = subtract(nums[0], nums[1])
        nums.pop(1)
    elif x == '*':
        nums[0] = multiply(nums[0], nums[1])
    elif x == 'denary':
        denary = [denaryConverter(format(y)) for y in nums]
        denary.append(True)


#output formatter for binary and denary
output = 'a'
negative = False
if denary[len(denary) - 1]:
    for x in range(0, len(nums)):
        if x == len(nums) - 1:
            output += str(denary[x])
        else:
            output += str(denary[x]) + ', '
    if nums[x][len(nums[x]) - 1]:
        output = '-' + output[1:]
elif denary[len(denary) - 1] == False:
    for x in nums:
        output += strFormat(x)

output = output[1:]
print(output)