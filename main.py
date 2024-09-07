from turtle import Screen, Turtle
import time

from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard


# screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

# player-boards
right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))

screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

# ball
ball = Ball()

# scoreboard with the central line
scoreboard = ScoreBoard()

screen.update()

game_over = False

while not game_over:
    ball.move()
    
    # detect collision of the ball with the top and bottom walls
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.baunce()
                       
    # detect collision of the ball with the paddles
    if ball.xcor() >= 330 and ball.distance(right_paddle) <= 50 or ball.xcor() <= -330 and ball.distance(left_paddle) <= 50:
        ball.hit()
    
    # right paddle misses the ball
    if ball.xcor() > 380: 
        scoreboard.l_point()
        ball.reset()
        ball.hit()
       
    
    # left paddle misses the ball
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset()
        ball.hit()
        
    screen.update()    
    time.sleep(ball.move_speed)
    

screen.exitonclick()