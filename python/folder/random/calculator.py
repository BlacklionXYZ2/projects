
l = True
word = ''
nums = []
num = 1
operators = ['*', '+', '/', '-']

while l == True:
    response = input()
    for x in response:
        word += x
        if x == ' ':
            word.rstrip()
            if word.isnumeric() == True:
                num = int(word)
                print(num)
                nums.append(num)
                word = ''
                num = 0
            elif word in operators:
             print(nums)




