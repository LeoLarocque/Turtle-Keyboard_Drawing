import turtle
import keyboard
print('"w" ^ "s" v "a" <- "d" -> "c" makes dot. "o" makes circle. "9" color to red. "^" penup. "v" pendown.')
screen = turtle.Screen()
screen.setup(1200, 800)
screen.bgcolor("yellow")
turtle1 = turtle.Turtle()
turtle1.shape("turtle")
"""turtle2 = turtle.Turtle()
turtle3 = turtle.Turtle()
turtle4 = turtle.Turtle()
turtle2.hideturtle()
turtle3.hideturtle()
turtle4.hideturtle()"""
while True:
    if keyboard.is_pressed("w"):
        turtle1.forward(10)
        """turtle2.forward(10)
        turtle3.forward(10)
        turtle4.forward(10)"""
    if keyboard.is_pressed("s"):
        turtle1.backward(10)
        """turtle2.backward(10)
        turtle3.backward(10)
        turtle4.backward(10)"""
    if keyboard.is_pressed("a"):
        turtle1.left(10)
        """turtle2.left(10)
        turtle3.left(10)
        turtle4.left(10)"""
    if keyboard.is_pressed("d"):
        turtle1.right(10)
        """turtle2.right(10)
        turtle3.right(10)
        turtle4.right(10)"""
    if keyboard.is_pressed("c"):
        turtle3.dot(30)
    if keyboard.is_pressed("o"):
        turtle4.circle(30)
    if keyboard.is_pressed("9"):
        turtle1.color("red")
        """turtle2.color("red")
        turtle3.color("red")
        turtle4.color("red")"""
    if keyboard.is_pressed("^"):
        turtle1.penup()
        """turtle2.penup()
        turtle3.penup()
        turtle4.penup()"""
    if keyboard.is_pressed("v"):
        turtle1.pendown()
        """turtle2.pendown()
        turtle3.pendown()
        turtle4.pendown()""" 
                     
        
        
