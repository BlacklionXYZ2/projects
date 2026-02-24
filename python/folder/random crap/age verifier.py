print("Please enter birth year")
reqAge = 18
year = 2023
age = int(input())
calcAge = year - age
if  calcAge >= reqAge:
    print("You can vote!")
else:
    print("You cannot vote, wait", reqAge - calcAge, "years.")