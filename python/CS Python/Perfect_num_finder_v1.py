limit = int(input())
# The highest limit I've found within a reasonable time is around 60,000

perf_nums = []

loops = 0

class num:
    n = 0
    factors = []

def factorise(data):
    global loops
    for x in range(1, data.n):
        loops += 1
        if data.n % x == 0:
            data.factors.append(x)

def find_perf(lim):
    global perf_nums, loops
    while num.n <= lim:
        loops += 1
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
end = len(perf_nums)

for x in range(0, end):
    loops += 1
    if x != end - 1:
        text += f' {perf_nums[x]},' 
    elif x == end - 1:
        text = text[:-1]
        text += f' and {perf_nums[x]}'

text = text[1:]

print(f'The perfect integers between 1 and {limit} are:{text}') 
print('loops:', loops) 