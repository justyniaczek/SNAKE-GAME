#snake project
import turtle
import time
import os
import random


delay =0.05
wn = turtle.Screen()
wn.title("Snake")
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.tracer(0) # turns off the screen updates

#snake head
head= turtle.Turtle()
head.speed(0)
head.penup()
head.goto(0,0)
head.shape("square")
head.color("pink")
head.direction="right"

#random
x= random.uniform(-280,280.0)
y= random.uniform(-280.,280.)
#food
food=turtle.Turtle()
food.speed(0)
food.penup()
food.goto(x,y)
food.shape("circle")
food.color("green")

# move functions
def go_up():

    if head.direction=="down":
        head.direction = "down"
    else:
        head.direction = "up"
def go_down():
    if head.direction == "up":
        head.direction = "up"
    else:
        head.direction = "down"
def go_left():
    if head.direction =="right":
        head.direction = "right"
    else:
        head.direction = "left"
def go_right():
    if head.direction =="left":
        head.direction="left"
    else:
        head.direction="right"

#keyboard bindings
wn.listen()
wn.onkeypress(go_up,"w")
wn.onkeypress(go_down,"s")
wn.onkeypress(go_right,"d")
wn.onkeypress(go_left, "a")

#move
def move():
    if head.direction=="up":
        y = head.ycor()
        head.sety(y + 20)
    elif head.direction == "down":
        y = head.ycor()
        head.sety(y -20)
    elif head.direction=="left":
        x = head.xcor()
        head.setx(x - 20)
    elif head.direction=="right":
        x = head.xcor()
        head.setx(x + 20)
#score
game_score =0
high_score=0
#string score
score=turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(-270,270)
score.write("Score:0  High score:0".format(game_score, high_score), align="left", font=("Courier", 15, "normal"))
segments=[]


#main game loop
while True:
    wn.update()
    time.sleep(delay)
    if head.distance(food)<20:
        game_score+=1
        high_score+=1
        score.clear()
        score.write("Score:{}  High score:{}".format(game_score,high_score), align="left",font=("Courier", 15, "normal"))
        x = random.randint(-280, 260)
        y = random.randint(-280, 260)
        food.goto(x, y)
        #adding new segment
        new_segment= turtle.Turtle()
        new_segment.speed(0)
        new_segment.color("grey")
        new_segment.shape("square")
        new_segment.penup()
        new_segment.goto(head.xcor(),head.ycor())
        delay-=0.0013
        segments.append(new_segment)       #???????????????
    if head.ycor() > 290 or head.ycor() <-290 or head.xcor() >290 or head.xcor()<-290:
        time.sleep(1.5)
        head.goto(0,0)
        head.direction="stop"
        segments.clear()
        game_score = 0
        delay = 0.05
        score.clear()
        score.write("Score:{}  High score:{}".format(game_score, high_score), align="left",font=("Courier", 15, "normal"))

    for index in range(len(segments)-1,0,-1):
        x=segments[index-1].xcor()
        y=segments[index-1].ycor()
        segments[index].goto(x,y)

    if len(segments) >0:
        x=head.xcor()
        y=head.ycor()
        segments[0].goto(x,y)
    move()

    for segment in segments:
        if segment.distance(head)<20:
            time.sleep(1.5)
            head.goto(0, 0)
            head.direction = "stop"

            for segmenti in segments:
                segments[0].goto(1000,1000)
            segments.clear()
            game_score=0
            delay = 0.05
            score.clear()
            score.write("Score:{}  High score:{}".format(game_score, high_score), align="left",font=("Courier", 15, "normal"))


    time.sleep(delay)
wn.mainloop()
