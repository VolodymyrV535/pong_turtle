from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "sky blue", "blue", "violet"]


class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.speed(0.1)
        self.move_speed = 0.1
        self.x_cor = 10
        self.y_cor = 10
        
        
    def move(self):
        new_x_cor = self.xcor() + self.x_cor
        new_y_cor = self.ycor() + self.y_cor
        self.goto(new_x_cor, new_y_cor)
        
        
    def baunce(self):
        self.y_cor *= -1
        
    
    def hit(self):
        self.x_cor *= -1
        self.move_speed = self.move_speed * 0.9
        
    
    def reset(self):
        self.goto(0, 0)
        self.color(random.choice(COLORS))
        self.move_speed = 0.1

        
        
