termnum = int(input('input term'))
fib = [1, 1]
for x in range(1, termnum):
    term = fib[x] + fib[x - 1]
    fib.append(fib[x] + fib[x - 1])
    print(term)