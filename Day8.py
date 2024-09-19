# print("Chuck Norris doesn't flush toilets; he scares the shit out of them.")
############2.1###########

#turtle graphic is an implementation that uses a style of proggramation object oriented
"""toto = turtle . Screen ()
toto . bgcolor ("black")
titi = turtle . Turtle ()
titi . color ("red")
for i in range (3) :
    titi . right (90)
titi . circle (42)
toto . exitonclick ()
#This code enable to draw a red circle
"""

###############2.3##############

"""""
def draw_polygon(sides):
    screen = turtle.Screen() # defines the turtle screen
    screen.bgcolor("white") # gives the color
polygon = turtle.Turtle() 
polygon.color("pink") 

angle = 360 / 3 # calcule l'angle de chaque coin du polygone
side_length = 100 


for _ in range(3): 
 polygon.forward(side_length) 
 polygon.right(angle) 
# draw_polygon(5)
"""
##################2.4#################

"""
import turtle
t = turtle.Screen()
ti = turtle.Turtle()
r=8

for i in range(100):
    ti.circle(r+i,35)

t.exitonclick()
"""
###############challenge###############
'''
import turtle
import colorsys

t = turtle.Turtle()



t.bgcolor("black")

t.speed(10)

t.pensize(2)

hue=0.0

t.hideturtle()

t.setpost(-130, -90)

for i in range(800):

    color = colorsys.hsv_to_rgb(hue,1,1)

    t.pencolor(color)

    hue +=0.005

    t.circle(190-i, 30)

    t.left(110*2)

    t.circle(190-i,30)

    t.left(60*2)

    t.tracer(10)

t.exitonclick()

'''
###############3.4############

'Done'

##############3.5#############







