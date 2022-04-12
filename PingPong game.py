import turtle

window = turtle.Screen()                     # to show the screen
window.title("Ping Pong game")               # name of game in window
window.bgcolor("black")                      # background colour
window.setup(width=800 , height=600)         # size of window
window.tracer(0)                             # to stop any update while run
# madrab1
madrab1 = turtle.Turtle()                    # make object from turtle to show the shape
madrab1.shape("square")                      # show how the shape will be
madrab1.speed(0)                             # set the speed of the animation
madrab1.penup()                              # stop the object from frawing lines
madrab1.color("red")                         # set color of shape
madrab1.goto(-350, 0)                        # the position of the object in window
madrab1.shapesize(5, 1)                      # the object size
# madrab 2
madrab2 = turtle.Turtle()
madrab2.shape("square")
madrab2.speed(0)
madrab2.penup()
madrab2.color("blue")
madrab2.goto(350,0)
madrab2.shapesize(5,1)
# ball
ball = turtle.Turtle()
ball.shape("circle")
ball.speed(0)
ball.penup()
ball.color("white")
ball.dx = 0.4
ball.dy = 0.4
# score
scor1=0
score2=0
score = turtle.Turtle()
score.speed(0)
score.color("white")
score.penup()
score.hideturtle()
score.goto(0,260)
score.write("Player one score= & Player two score=", align="center", font=("Courier", 24, "normal"))


# functions to move 2 madrabs
def madrab1_up():
    y = madrab1.ycor()
    y += 40
    madrab1.sety(y)
def madrab1_down():
    y = madrab1.ycor()
    y -= 40
    madrab1.sety(y)

def madrab2_up():
    y = madrab2.ycor()
    y += 40
    madrab2.sety(y)
def madrab2_down():
    y = madrab2.ycor()
    y -= 40
    madrab2.sety(y)

window.listen()
window.onkeypress(madrab1_up,"w")
window.onkeypress(madrab1_down,"s")
window.onkeypress(madrab2_up,"Up")
window.onkeypress(madrab2_down,"Down")

# the game loop
while True:
    window.update()                         # to make update when game end
    # move the ball
    ball.sety(ball.ycor()+ball.dy)
    ball.setx(ball.xcor() + ball.dx)
    # border check
    if ball.ycor()>300:
        ball.sety(300)
        ball.dy*=-1
    if ball.ycor()<-300:
        ball.sety(-300)
        ball.dy*=-1
    if ball.xcor()>400:
        ball.sety(400)
        ball.dx*=-1
        scor1 += 1
        score.clear()
        score.write("Player one score={} & Player two score={}".format(scor1,score2), align="center", font=("Courier", 24, "normal"))
    if ball.xcor() < -400:
        ball.sety(-400)
        ball.dx *= -1
        score2 +=1
        score.clear()
        score.write("Player one score={} & Player two score={}".format(scor1,score2), align="center", font=("Courier", 24, "normal"))

    if (ball.xcor()>340 and ball.xcor()<350)and(ball.ycor()<madrab2.ycor()+45 and ball.ycor()>madrab2.ycor()-50):
        ball.setx(340)
        ball.dx *=-1

    if (ball.xcor()<-340 and ball.xcor()>-350)and(ball.ycor()<madrab1.ycor()+40 and ball.ycor()>madrab1.ycor()-50):
        ball.setx(-340)
        ball.dx *=-1
X