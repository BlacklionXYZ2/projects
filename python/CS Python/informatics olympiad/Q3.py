print('Oscar Hunt Brown, Ashby School')
response = int(input())
config = {'n': response if response >= 1 and response <= 2**63 else 0}
n = config['n']

raindrop_numbers = []

for x in range(n):
    previous_digit = None
    raindrop_number = False
    for current_digit in str(x):
        if previous_digit != None:
            if previous_digit > int(current_digit) and not raindrop_number:
                raindrop_number = True
            elif previous_digit > int(current_digit) and raindrop_number:
                raindrop_number = False
                break
        previous_digit = int(current_digit)

    if raindrop_number:
        raindrop_numbers.append(x)

print(len(raindrop_numbers))