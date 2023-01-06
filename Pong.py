import turtle

window=turtle.Screen()
window.title("Denis's Pong Game")
window.bgcolor('white')
window.setup(width=800,height=600)
window.tracer(0)

#score
player1=0
player2=0

#Red paddle(Player1)
paddle1=turtle.Turtle()
paddle1.speed(0)
paddle1.shape('square')
paddle1.color('red')
paddle1.shapesize(stretch_wid=5,stretch_len=1)
paddle1.penup()
paddle1.goto(-350,0)

#Blue paddle(Player2)
paddle2=turtle.Turtle()
paddle2.speed(0)
paddle2.shape('square')
paddle2.color('blue')
paddle2.shapesize(stretch_wid=5,stretch_len=1)
paddle2.penup()
paddle2.goto(350,0)

#Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('orange')
ball.penup()
ball.goto(0,0)
ball.dx = 2
ball.dy = -2

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("Black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))

#function
def Paddle1up():
	y=paddle1.ycor()
	y += 20
	paddle1.sety(y)
def Paddle1down():
	y=paddle1.ycor()
	y -= 20
	paddle1.sety(y)

def Paddle2down():
	y=paddle2.ycor()
	y -= 20
	paddle2.sety(y)
def Paddle2up():
	y=paddle2.ycor()
	y += 20
	paddle2.sety(y)



#controls 
window.listen()
window.onkeypress(Paddle1up,'w')
window.onkeypress(Paddle1down,'s')
window.onkeypress(Paddle2down,'Down')
window.onkeypress(Paddle2up,'Up')



#Game loop
while True:
    window.update()
    
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Top and bottom
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1
    elif ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1
    

    # Left and right
    if ball.xcor() > 350:
        player1 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player1, player2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    elif ball.xcor() < -350:
        player2 += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player1, player2), align="center", font=("Courier", 24, "normal"))
        ball.goto(0, 0)
        ball.dx *= -1

    # Paddle and ball collisions
    if ball.xcor() < -340 and ball.ycor() < paddle1.ycor() + 50 and ball.ycor() > paddle1.ycor() - 50:
        ball.dx *= -1 
    
    elif ball.xcor() > 340 and ball.ycor() < paddle2.ycor() + 50 and ball.ycor() > paddle2.ycor() - 50:
        ball.dx *= -1