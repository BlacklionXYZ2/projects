import random 
guesses = 2
correct = 0 
computer = random.randrange(1,10) 
while guesses >0:
    print("guess a number between 1 and 10:")
    user = int(input())
    if user > computer: 
        above = user - computer 
        print("Your guess was " , above, "above the generated number.")
    elif user < computer: 
        below = computer - user
        print("Your guess was " , below, "below the generated number.")
    else: 
        print("Correct!") 
        correct = 1
    while correct == 1:
        import random
        guesses = 3
        correct = 0
        computer = random.randrange(1,10)


