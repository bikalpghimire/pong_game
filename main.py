import time
from turtle import Screen
from scoreboard import Scoreboard
from ball import Ball
from paddle import Paddle

screen = Screen()
screen.delay(0)
screen.setup(800, 600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(right_paddle.up, "Up")
screen.onkeypress(right_paddle.down, "Down")
screen.onkeypress(left_paddle.up, "w")
screen.onkeypress(left_paddle.up, "W")
screen.onkeypress(left_paddle.down, "s")
screen.onkeypress(left_paddle.down, "S")
screen.listen()

game_is_on = True
while game_is_on:
    screen.listen()
    screen.onkey(right_paddle.up, "Up")
    screen.onkey(right_paddle.down, "Down")
    screen.onkey(left_paddle.up, "w")
    screen.onkey(left_paddle.up, "W")
    screen.onkey(left_paddle.down, "s")
    screen.onkey(left_paddle.down, "S")
    screen.listen()
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_wall()
    elif ball.xcor() > 330 and ball.distance(right_paddle) < 50 or ball.xcor() < -330 and ball.distance(
            left_paddle) < 50:
        ball.bounce_paddle()
        ball.move()

    elif ball.xcor() > 400:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor() < -400:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
