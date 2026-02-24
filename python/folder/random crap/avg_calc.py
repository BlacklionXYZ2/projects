dataNum = [1.3, 1.76, 1.8, 1.2, 1.963, 2]
dataBool = [True, True, True, False, False, False]
dataStr = ['kjghfvhv', 'car', 'banana', 'aren']
class strNum:
    a = 1
    b = 2
    c = 3
    d = 4
    e = 5
    f = 6
    g = 7
    h = 8
    i = 9
    j = 10
    k = 11
    l = 12
    m = 13
    n = 14
    o = 15
    p = 16
    q = 17
    r = 18
    s = 19
    t = 20
    u = 21
    v = 22
    w = 23
    x = 24
    y = 25
    z = 26

def avgNum(nums):
    length = 0
    total = 0
    for x in nums:
        length += 1
        total += x
    average = total / length
    return average

def avgBool(data):
    trues = 0
    falses = 0

    for x in data:
        if x == True:
            trues += 1
        elif x == False:
            falses += 1

    if trues > falses:
        result = True
    elif falses > trues:
        result = False
    elif falses == trues:
        result = 'Neutral'

    return result

def avgStr(data):
    length = 0
    lenStr = 0
    total = 0
    for x in data:
        length += 1
        lenStr += len(x)
        total += lenStr
        lenStr = 0
    avg = total / length
    return avg
        

# print(avgNum(dataNum))

# print(avgBool(dataBool))

# print(avgStr(dataStr))
