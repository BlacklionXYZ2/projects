import random
import turtle

start = True
turtle.speed(10)

while start == True:
    direction = random.randint(1, 2)
    dist = random.randint(1, 40)
    angle = random.randint(1, 180)
    red = random.randrange(0, 100, 1)
    green = random.randrange(0, 100, 1)
    blue = random.randrange(0, 100, 1)

    #direction loop
    if direction == 1:
        turtle.right(float(angle))
    elif direction == 2:
        turtle.left(float(angle))
    turtle.forward(float(dist))
    turtle.color(red / 100, green / 100, blue / 100)