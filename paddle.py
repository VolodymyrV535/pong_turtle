from turtle import Turtle


class Paddle(Turtle):
    
    def __init__(self, position):
        super().__init__()
        self.position = position
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color("white")
        self.penup()
        self.goto(position)          
    
    def up(self):
        changed_ycor = self.ycor() + 20
        self.goto(self.xcor(), changed_ycor)
            
    
    
    def down(self):
        changed_ycor = self.ycor() - 20
        self.goto(self.xcor(), changed_ycor)

