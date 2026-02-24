num = input()
num = num[::-1]

split_num = []
inputs = []
last_idx = 0


for x in range(0, len(num) + 1):
    if x % 2 == 0:
        split_num.append(num[last_idx : x])
        last_idx = x
    elif x == len(num):
        split_num.append(num[len(num) - 1:])

split_num.pop(0)

for x in range(0, len(split_num)):
    if len(split_num[x]) == 1:
        split_num[x] += '0'

for x in range(0, len(split_num)):
    inputs.append(split_num[len(split_num) - x - 1])
print(inputs, split_num)

const = '01'
temp = ''
temp2 = ''
padConst = ''
output = 'a'


def binary_subtracter(num1, num2):
    print(num1, num2)
    out = 'a'
    for x in range(0, len(num1) - 1):
        if num1[x] == '0' and num2[x] == '0':
            out += '0'
            print(1)
        elif num1[x] == '0' and num2[x] == '1':
            print(2)
            try:
                if num1[x + 1] == '1':
                    num1[x + 1] = '0'
                    out += '1'
                    print('carried 1')
                elif num1[x + 1] == '0':
                    print('operation impossible')
                    return out[1:], '0'
            except IndexError:
                print('index error')
                return out[1:], '0'
        elif num1[x] == '1' and num2[x] == '0':
            print(3)
            out += '1'
        elif num1[x] == '1' and num2[x] == '1':
            print(4)
            out += '0'
        return [out[1:], '1'] 
    
for x in inputs:
    temp2 = temp + x
    print(temp2)
    padConst = const
    if len(temp2) > len(const):
        print(len(temp2) - len(const))
        for x in range(0, len(temp2) - len(const)):
            padConst += '0'
    print(padConst)

    store = binary_subtracter(temp2, padConst)
    temp = store[0]
    output += store[1]
    const += store[1]
    print(store, temp, output, const)

print(output[1:])