size = 4
samples = 100
channels = 1
time = 150

total = 0
x = 1

while x <= time:
    total += size * samples
    x += 1
    
print((total / 1000) * channels)
