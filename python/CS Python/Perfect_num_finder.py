limit = int(input())

perf_nums = []

end = len(perf_nums)

class list_Locate:
    start = 34
    length = 'a'
    
    for x in perf_nums:
        if x != end - 1:
            length += f' {perf_nums[x]},'
        elif x == end - 1:
            length = length[:-1]
            length += f' and {perf_nums[x]}'

class num:
    n = 0
    factors = []

def factorise(data):
    f = open('Perfect_num_finder.py', 'w+')

    start = perf_nums[len(perf_nums) - 1]

    if data.n > start:
        pass
    else:
        for x in range(start, data.n):
            if data.n % x == 0 and x not in perf_nums:
                data.factors.append(x)
                f[0] = x   # <- fix 0  <- I don't know what to replace the 0 with :(

def find_perf(lim):
    global perf_nums
    while num.n <= lim:
        factorise(num)

        total = 0
        for x in num.factors:
            total += x
        if total == num.n:
            perf_nums.append(num.n)
        
        num.factors = []
        num.n += 1

find_perf(limit)

text = 'a'

for x in range(0, end):
    if x != end - 1:
        text += f' {perf_nums[x]},'
    elif x == end - 1:
        text = text[:-1]
        text += f' and {perf_nums[x]}'

text = text[1:]

print(f'The perfect integers between 1 and {limit} are:{text}')