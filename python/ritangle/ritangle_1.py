
seq1 = list(range(1, 9))
seq2 = list(range(10, 21))
seq3 = list(range(1, 10))
S = 0
T = 0

for x in seq1:
    for y in seq2:
        for z in seq3:
            S += int(f'{x}{y}{z}')
            T += x * y * z

print(S / T)
# answer is 13.79