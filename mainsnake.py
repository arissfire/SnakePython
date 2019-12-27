import turtle
import time
import random
import pygame


#### Screen #####
ar =turtle.Screen()
ar.bgcolor("green")
ar.setup(width=600, height=600)
ar.tracer(0)
ar.title("SNAKE GAME")


ar.mainloop()


score= turtle.Turtle()
score.speed(0)
score.shape("square")
score.color("blue")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Score: 0  High Score: 0", align="centter", font=("Courier", 28, "normal"))



