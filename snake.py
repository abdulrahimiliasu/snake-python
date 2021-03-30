from turtle import Turtle

POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
BOUND = 285
MOVE = 20


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in POSITIONS:
            self.create_part(position)

    def create_part(self, position):
        square = Turtle(shape='square')
        square.penup()
        square.color('white')
        square.goto(position)
        self.body.append(square)

    def increase_part(self):
        self.create_part(self.body[-1].position())

    def move(self):
        for i in range(len(self.body) - 1, 0, -1):
            x = self.body[i - 1].xcor()
            y = self.body[i - 1].ycor()
            self.body[i].goto(x, y)
        head = self.body[0]
        head.forward(MOVE)

    def reset_snake(self):
        for part in self.body:
            part.goto(1000, 1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def hit_wall(self):
        if self.head.xcor() > BOUND or self.head.xcor() < -BOUND or self.head.ycor() > BOUND or self.head.ycor() < -BOUND:
            return True

    def collides(self):
        for part in self.body[1:]:
            if self.head.distance(part) < 10:
                return True

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)
