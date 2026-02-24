import random
print("Guess a number between 1 and 10")
computer = random.randrange(1, 10)
attempts = 2
guess = int(input())
retNum = computer - guess
def compare():
    if retNum <= 0:
        retNum == guess - computer
    return retNum
def reset():
    computer == random.randrange(1, 10)
    attempts == 2
    guess == int(input())
    print("Guess a number between 1 and 10")
while attempts >= 0:
    if guess == computer:
        print("Well done! The number was", computer,".")
        reset()
    elif guess != computer:
        print("Wrong, try again!")
        print("You were", compare(), "away!")
        guess == int(input())
        attempts -= 1
if attempts == 0 and guess != computer:
    print("You have run out of guesses, the number was", computer,".")
    reset()