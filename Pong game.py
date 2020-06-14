import turtle, winsound, time


def paddle_a_up():
    if paddle_a.ycor() < 190:
        y = paddle_a.ycor()
        y += 15
        paddle_a.sety(y)

def paddle_a_down():
    if paddle_a.ycor() > -235:
        y = paddle_a.ycor()
        y -= 15
        paddle_a.sety(y)

def paddle_b_up():
    if paddle_b.ycor() < 190:
        y = paddle_b.ycor()
        y += 15
        paddle_b.sety(y)

def paddle_b_down():
    if paddle_b.ycor() > -235:
        y = paddle_b.ycor()
        y -= 15
        paddle_b.sety(y)


Player_a = input('Enter name 1: ')
Player_b = input('Enter name 2: ')

wn = turtle.Screen()
wn.title('Pong Game')
wn.bgcolor('Black')
wn.setup(width=800, height=600)
wn.tracer(0)


# Paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape('square')
paddle_a.color('White')
paddle_a.penup()
paddle_a.goto(-390,0)
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)


# Paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('White')
paddle_b.penup()
paddle_b.goto(383,0)
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)


# Ball
ball=turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('Red')
ball.penup()
ball.goto(0,0)
ball.shapesize(stretch_wid=0.5, stretch_len=0.5)
ball.dx=0.8
ball.dy=0.8


# UpperLine
line1 = turtle.Turtle()
line1.speed(0)
line1.shape('square')
line1.color('Blue')
line1.penup()
line1.goto(0,250)
line1.shapesize(stretch_wid=0.2,stretch_len=40)

# Lower line
line2 = turtle.Turtle()
line2.speed(0)
line2.shape('square')
line2.color('Blue')
line2.penup()
line2.goto(0,-295)
line2.shapesize(stretch_wid=0.2,stretch_len=40)

# Pen
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.color('White')
pen1.penup()
pen1.hideturtle()
pen1.goto(0,260)
pen1.write(f'{Player_a}  vs {Player_b} ',align='center',font=('Courier',24))

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.color('White')
pen2.penup()
pen2.hideturtle()
pen2.goto(0,0)

wn.listen()
wn.onkeypress(paddle_a_up,'w')
wn.onkeypress(paddle_a_down,'s')
wn.onkeypress(paddle_b_up,'Up')
wn.onkeypress(paddle_b_down,'Down')


while True:
    wn.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 245 or ball.ycor() < -290:
        ball.dy *= -1
        winsound.PlaySound('Bounce2.wav',winsound.SND_ASYNC)

    if ball.xcor() > 392 or ball.xcor() < -397:
        winsound.PlaySound('Lost3.wav', winsound.SND_ASYNC)
        if ball.xcor() > 392:
            pen1.clear()
            pen1.write(f'{Player_a}  vs {Player_b} ', align='center', font=('Courier', 24))
            pen2.write(f'{Player_a}: Won ',align='center',font=('Courier',24))
            time.sleep(1)
            pen2.clear()
            pen2.write('Ready for next game!',align='center',font=('Courier',24))
            time.sleep(0.5)
            pen2.clear()
            pen2.write('3',align='center',font=('Courier',24))
            time.sleep(0.5)
            pen2.clear()
            pen2.write('2',align='center',font=('Courier',24))
            time.sleep(0.5)
            pen2.clear()
            pen2.write('1',align='center',font=('Courier',24))
            time.sleep(0.5)
            pen2.clear()
        else:
            pen1.clear()
            pen1.write(f'{Player_a}  vs {Player_b} ',align='center',font=('Courier',24))
            pen2.write(f'{Player_b}: Won',align='center',font=('Courier',24))
            time.sleep(1)
            pen2.clear()
            pen2.write('Ready for next game!', align='center', font=('Courier', 24))
            time.sleep(0.5)
            pen2.clear()
            pen2.write('3', align='center', font=('Courier', 24))
            time.sleep(0.5)
            pen2.clear()
            pen2.write('2', align='center', font=('Courier', 24))
            time.sleep(0.5)
            pen2.clear()
            pen2.write('1', align='center', font=('Courier', 24))
            time.sleep(0.5)
            pen2.clear()

        ball.goto(0,0)
        ball.dx *= -1


    # Collision
    if (ball.xcor() > 373 and ball.xcor() < 395 and ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50) or (ball.xcor() < -380 and ball.xcor() > -397 and ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        ball.dx *= -1
        if ball.xcor()>373:
            ball.goto(370,ball.ycor())
        else:
            ball.goto(-377,ball.ycor())
        winsound.PlaySound('Bounce.wav',winsound.SND_ASYNC)
