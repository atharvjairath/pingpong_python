import turtle
import os

wn = turtle.Screen()
wn.title("Ping Pong")
wn.bgcolor("black")
wn.setup(width=800,height=600)
wn.tracer(0)

scoreA=0
scoreB=0
# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.penup()
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.goto(-350,0)





# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.penup()
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.goto(350,0)

# Ball
Ball = turtle.Turtle()
Ball.speed(0)
Ball.shape("square")
Ball.color("white")
Ball.penup()
Ball.goto(0,0)
Ball.dx=2
Ball.dy=-2

#Pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier",24,"normal"))

# function

def paddle_a_up():
    y=paddle_a.ycor()
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor()
    y-=20
    paddle_a.sety(y)

def paddle_b_up():
    y=paddle_b.ycor()
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor()
    y-=20
    paddle_b.sety(y)

#keybaord binding
wn.listen()
wn.onkeypress(paddle_a_up,'e')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')

#Main Game loop
while True:
    wn.update()

    #move the ball
    Ball.setx(Ball.xcor()+Ball.dx)
    Ball.sety(Ball.ycor()+Ball.dy)

    # Border checking
    if Ball.ycor() >290:
        Ball.sety(290)
        Ball.dy *=-1
        os.system("afplay bounce.wav&")

    if Ball.ycor() < -290:
        Ball.sety(-290)
        Ball.dy *=-1
        os.system("afplay bounce.wav&")

    if Ball.xcor() >390:
        Ball.goto(0,0)
        Ball.dx *=-1
        scoreA+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA,scoreB),align="center", font=("Courier", 24, "normal"))

    if Ball.xcor() < -390:
        Ball.goto(0,0)
        Ball.dx *=-1
        scoreB+=1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(scoreA, scoreB), align="center", font=("Courier", 24, "normal"))

    #Paddle and Ball collison
    if (Ball.xcor() >340 and Ball.xcor() <350 and (Ball.ycor() < paddle_b.ycor() + 50) and (Ball.ycor()>paddle_b.ycor()-50)):
        Ball.setx(340)
        Ball.dx *=-1
        os.system("afplay bounce.wav&")


    if (Ball.xcor() <-340 and Ball.xcor() >-350 and (Ball.ycor() < paddle_a.ycor() + 50) and (Ball.ycor()>paddle_a.ycor()-50)):
        Ball.setx(-340)
        os.system("afplay bounce.wav&")
        Ball.dx *=-1

