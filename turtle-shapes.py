import turtle
import random

s = turtle.Screen()
#s.bgcolor('black')
fred = turtle.Pen()
fred.color('black')
fred.width(5)
fred.turtlesize(3,3)
fred.shape('turtle')
fred.speed(0)

'''for i in range(4):
    fred.forward(200)
    fred.left(90)'''

#fred.circle(100)

#fred.dot(200)

'''for i in range(6):
    fred.forward(150)
    fred.left(60)'''

'''for i in range(3):
    fred.forward(150)
    fred.left(120)'''

colors = ['red', 'green', 'pink', 'turquoise', 'grey', 'blue', 'orange', 'black']

shapes = ['square', 'triangle', 'circle', 'dot', 'hexagon']
index = 0

'''for i in range(100):
    #fred.color(colors[index])
    turtleColor = random.choice(colors)
    print(turtleColor)
    fred.color(turtleColor)
    fred.circle((5*i))
    fred.left(10)
    index += 1
    if index == 8:
        index = 0'''
coordinates = list(range(-200,201))
for i in range(50):
    shape = random.choice(shapes)
    print(shape)
    turtleColor = random.choice(colors)
    print(turtleColor)
    fred.color(turtleColor)
    x = random.choice(coordinates)
    y = random.choice(coordinates)
    print(x,y)
    fred.penup()
    fred.setposition(x,y)
    fred.pendown()
    if shape == 'square':
        for i in range(4):
            fred.forward(100)
            fred.left(90)
    elif shape == 'triangle':
        for i in range(3):
            fred.forward(100)
            fred.left(120)
    elif shape == 'circle':
        fred.circle(100)
    elif shape == 'dot':
        fred.dot(100)
    else:
        for i in range(6):
            fred.forward(100)
            fred.left(60)
