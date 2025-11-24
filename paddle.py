from turtle import Turtle

class Paddle(Turtle):

    MOVE_DISTANCE = 20
    WIDTH = 5
    LENGTH = 1

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=self.WIDTH, stretch_len=self.LENGTH)
        self.penup()
        self.speed("fastest")
        self.goto(position)

    def go_up(self):
        new_y = self.ycor() + self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - self.MOVE_DISTANCE
        self.goto(self.xcor(), new_y)
