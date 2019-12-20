# -*- coding: utf-8 -*-
"""
Created on Fri Dec 20 10:40:37 2019

@author: Félix FERRAND
"""
import numpy
import turtle 
from easygui import *

# Initialisation du jeu
ts = turtle.getscreen()
ts.clear()
ts.bgpic("champcourse2.gif")

ts.title("Bienvenue à la course des tortues !")
ts.setup (width=1400, height=800, startx=0, starty=0)

turtle.speed = 0

# function
def initTurtle(myTurtle, color, posY):
    myTurtle.color(color)
    myTurtle.shape("turtle")
    myTurtle.up()
    myTurtle.goto(200, posY)
# end function
    
# function
def arrived(myTurtle):
    if (myTurtle.xcor() > 630):
        return True
    else:
        return False        
# end function
        
# function
def randomSpeed():
    return numpy.random.randint(20,50)      
# end function
        
# function
def run(turtle, turtleName):
    if (not arrived(turtle)):
        turtle.fd(randomSpeed())
    if (arrived(turtle) and not turtleName in classement):
        classement.append(turtleName)     
# end function


Splinter = turtle.Turtle()
initTurtle(Splinter, "Dark Slate Gray", 325)

Leonardo = turtle.Turtle()
initTurtle(Leonardo, "Deep Sky Blue", 160)

Raphaelo = turtle.Turtle()
initTurtle(Raphaelo, "Red", 0)

Donatello = turtle.Turtle()
initTurtle(Donatello, "Purple", -135)

Michelangelo = turtle.Turtle()
initTurtle(Michelangelo, "Orange", -295)

prono1 = enterbox(msg='Qui sera le vainqueur ?', title='Joueur 1', default='')
prono2 = enterbox(msg='Qui sera le vainqueur ?', title='Joueur 2', default='')

classement = [];

while (not arrived(Splinter) or not arrived(Leonardo) or not arrived(Raphaelo) or not arrived(Donatello) or not arrived(Michelangelo)):
    
    run(Splinter, "1")
    run(Leonardo, "2")
    run(Raphaelo, "3")
    run(Donatello, "4")
    run(Michelangelo, "5")

turtle_arbitre = turtle.Turtle()
turtle_arbitre.up()
turtle_arbitre.goto(0,0)
turtle_arbitre.color("Black")

if (prono1 == classement[0]):
    turtle_arbitre.write("Le joueur 1 a remporte son pari", move=True, align="center", font=("Arial", 16, "normal"))
turtle_arbitre.goto(0,-25)
if (prono2 == classement[0]):
    turtle_arbitre.write("Le joueur 1 a remporte son pari", move=True, align="center", font=("Arial", 16, "normal"))
for i in classement:
    turtle_arbitre.goto(0,-25*i)
    turtle_arbitre.write(str(i)+" : tortue n°"+classement[i], move=True, align="center", font=("Arial", 16, "normal"))


