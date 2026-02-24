import random 
guesses = 2
correct = 0 
computer = random.randrange(1,10) 
hard = 0 
while guesses >0: 
    while hard == 1: 
        print ("Guess the number between 1 and 100:") 
        user = int(input()) 
        hard = 1 
    while hard == 0: 
        print ("Guess the number between 1 and 10:") 
        user = int(input())
        hard = 0 
    if user == 11: 
        print("You have now entered HardMode:")
        print("You must now guess a number between 1 and 100") 
        import random 
        guesses = 3
        correct = 0 
        computer = random.randrange(1,100) 
        hard = 1
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
        guesses = 2
        correct = 0
        computer = random.randrange(1,10) 
        hard = 0
        while hard == 1: 
            import random 
            guesses = 3 
            correct = 0 
            computer = random.randrange(1,100)
            hard = 1

