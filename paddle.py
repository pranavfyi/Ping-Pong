from turtle import Turtle


class Paddle(Turtle):

    MOVE_DISTANCE = 30

    DASH_DISTANCE = 30
    WIDTH = 5
    LENGTH = 1

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        
        self.color("lime green")
        self.shapesize(stretch_wid=self.WIDTH, stretch_len=self.LENGTH)
        self.penup()
        self.speed("fastest")
        self.goto(position)
       
        self.initial_x = position[0]

    def go_up(self):
    
        if self.ycor() < 240:
            new_y = self.ycor() + self.MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
    
        if self.ycor() > -240:
            new_y = self.ycor() - self.MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def dash(self):
        """Moves the paddle horizontally (closer to the center)."""

      
        if self.initial_x > 0:

            new_x = self.xcor() - self.DASH_DISTANCE
        else:
       
            new_x = self.xcor() + self.DASH_DISTANCE

        
        if abs(new_x) < 300:  
            self.goto(new_x, self.ycor())

      
