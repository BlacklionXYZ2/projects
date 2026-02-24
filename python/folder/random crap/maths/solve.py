
a = 1
b = 1
n = 1
ab = None
ni = None


def bUp():
    global b, ab, a, n, ni
    b += 1
    ab = a / b
    ni = ((8 * n) + 8) / ((6 * n) + 6)

    if ab == ni:
        print(a, b)
        

for x in range(100):
    a += 1
    n += 1
    ab = a / b
    ni = ((8 * n) + 8) / ((6 * n) + 6)

    if ab == ni:
        print(a, b)
    else:
        bUp()