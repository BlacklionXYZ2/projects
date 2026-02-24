 #importing
import random

#setting up main var
f = True
wl = None
guess = None

#setting up func
def wlfun():
    if wl == "win":
        print("you win!!! it was", guess)
    elif wl == "lose":
        print("You lose try again. btw it was", guess + 1)
    else:
        print("err")


def rig(target):
    if wl != "win" or "lose":
        num = random.randint(1, target)
        if guess == num:
            print("You win!!! it was", num)
        else:
            print("You lose try again. btw it was", num)
    else:
        wlfun()
        
#main progaram
while f == True:
    money = int(input("They put in > > > "))
    guess = int(input("And they guessed > > > "))
    wl = input("Override whether they win or lose > > > ")

    if money in range(1,5):
        rig(20)
            
    elif money in range(6,10):
        rig(12)

    elif money in range(11,16):
        rig(7)
            
    else:
        print("Guess was too low or high")

    print('')
        