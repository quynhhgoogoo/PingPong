import turtle

#Set up
win = turtle.Screen()  #initialize window
win.title("Pong")
win.bgcolor("black")
win.setup(width = 800, height = 600)
win.tracer(0)  #stop window from updating automatically

#Score calculation
score1 = 0
score2 = 0

#Paddle 1
paddle1 = turtle.Turtle()
paddle1.speed(0)
paddle1.shape("square")
paddle1.color("white")
paddle1.shapesize(stretch_wid = 6, stretch_len = 1)
paddle1.penup()
paddle1.goto(-380, 0)

#Paddle 2
paddle2 = turtle.Turtle()
paddle2.speed(0)
paddle2.color("white")
paddle2.shape("square")
paddle2.shapesize(stretch_wid = 6, stretch_len = 1)
paddle2.penup()
paddle2.goto(380, 0)

#Ball
ball = turtle.Turtle()
ball.speed(0)
ball.color("white")
ball.shape("circle")
#Ball movement
ball.xspeed = 0.2
ball.yspeed = 0.2

#Score 
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.hideturtle
score.penup()
score.goto(0,250)
score.write("Ping:0    Pong:0", align ="center", font =("Courier", 12, "normal"))

#Main game function
def paddle1_up():
    y = paddle1.ycor()
    y = y+10
    paddle1.sety(y)

def paddle1_down():
    y = paddle1.ycor()
    y = y-10
    paddle1.sety(y)

def paddle2_up():
    y = paddle2.ycor()
    y = y+10
    paddle2.sety(y)

def paddle2_down():
    y = paddle2.ycor()
    y = y-10
    paddle2.sety(y)
    
#Keyboard binding
win.listen()
win.onkeypress(paddle1_up, "w")
win.onkeypress(paddle1_down, "s")
win.onkeypress(paddle2_up, "Up")
win.onkeypress(paddle2_down, "Down")

#Game loop
while True:
    win.update()

    #Move the ball
    ball.penup()
    ball.setx(ball.xspeed + ball.xcor())
    ball.sety(ball.yspeed + ball.ycor())

    #Build Wall
    if ball.ycor() > 300:
        #ball.sety(300)
        ball.yspeed = -ball.yspeed

    if ball.ycor() < -300:
        #ball.sety(-300)
        ball.yspeed = -ball.yspeed

    if ball.xcor() > 400:
        ball.goto(0,0)
        ball.xspeed = - ball.xspeed
        score1 = score1 + 1
        score.clear()
        score.write("Ping:{}   Pong:{}".format(score1, score2), align ="center", font =("Courier", 12, "normal"))

    if ball.xcor() < -400:
        ball.goto(0,0)
        ball.xspeed = - ball.xspeed
        score2 = score2 + 1
        score.clear()
        score.write("Ping:{}   Pong:{}".format(score1, score2), align ="center", font =("Courier", 12, "normal"))

    #Paddle and ball collision
    if ball.xcor() < -380 and (ball.ycor() < paddle1.ycor() + 54 and ball.ycor() > paddle1.ycor() - 54):
        ball.xspeed = - ball.xspeed
        
    if ball.xcor() > 380 and (ball.ycor() < paddle2.ycor() + 54 and ball.ycor() > paddle2.ycor() - 54):
        ball.xspeed = - ball.xspeed
