import turtle
import time
import random
import pygame


#### Screen #####
ar =turtle.Screen()
ar.bgcolor("#78d742")
ar.setup(width=600, height=600)
ar.tracer(0)
ar.title("SNAKE GAME")



### Đầu Snake ###
head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("#000000")
head.penup()
head.goto(0,0)
head.direction = "stop"

### Food ###
food = turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("red")
food.penup()
food.goto(0,100)

segments = []

### Điểm số ###
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Điểm: 0  Kỷ Lục: 0", align="center", font=("Courier", 24, "normal"))

score = 0
high_score = 0
delay = 0.05
### Functions ###
def go_up():
    if head.direction != "down":
        head.direction = "up"

def go_down():
    if head.direction != "up":
        head.direction = "down"

def go_left():
    if head.direction != "right":
        head.direction = "left"

def go_right():
    if head.direction != "left":
        head.direction = "right"

def move():
    if head.direction == "up":
        y = head.ycor()
        head.sety(y + 20)

    if head.direction == "down":
        y = head.ycor()
        head.sety(y - 20)

    if head.direction == "left":
        x = head.xcor()
        head.setx(x - 20)

    if head.direction == "right":
        x = head.xcor()
        head.setx(x + 20)
###Di chuyển###
ar.listen()
ar.onkeypress(go_up, "w")
ar.onkeypress(go_down, "s")
ar.onkeypress(go_left, "a")
ar.onkeypress(go_right, "d")

### Main game ###
while True:
    ar.update()

    if head.xcor()>290 or head.xcor()<-290 or head.ycor()>290 or head.ycor()<-290:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"

        for segment in segments:
            segment.goto(1000, 1000)
        
    
        segments.clear()

        ###Reset điểm số###
        score = 0

        ### Reset delay ###
        delay = 0.1

        pen.clear()
        pen.write("Điểm: {}  Kỷ Lục: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 


    ### CheckFood ###
    if head.distance(food) < 20:
        ### Random thức ăn###
        x = random.randint(-290, 290)
        y = random.randint(-290, 290)
        food.goto(x,y)

        ### Tạo segment (thân) ###
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("#0069ca")
        new_segment.penup()
        segments.append(new_segment)

        delay -= 0.001

        ### Tăng điểm score###
        score += 1

        if score > high_score:
            high_score = score
        
        pen.clear()
        pen.write("Điểm: {}  Kỷ Lục: {}".format(score, high_score), align="center", font=("Courier", 24, "normal")) 

    
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)


    if len(segments) > 0:
        x = head.xcor()
        y = head.ycor()
        segments[0].goto(x,y)

    move()    

   
    for segment in segments:
        if segment.distance(head) < 20:
            time.sleep(1)
            head.goto(0,0)
            head.direction = "stop"
        
            ### Hide segments###
            for segment in segments:
                segment.goto(1000, 1000)
        
            ### Xoá segments###
            segments.clear()

            ### Reset điểm số bằng 0 ban đầu ###
            score = 0

            ### Reset delay ###
            delay = 0.1
        
            ### Cập nhật điểm số ###
            pen.clear()
            pen.write("Điểm: {}  Kỷ Lục: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))

    time.sleep(delay)
ar.mainloop()






