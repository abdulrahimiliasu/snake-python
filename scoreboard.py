from turtle import Turtle

ALIGNMENT = 'left'
FONT = ('Courier', 20, 'bold')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open('data.txt', mode='r') as data:
            self.high_score = int(data.read())
        self.color('white')
        self.penup()
        self.hideturtle()
        self.goto(-50, 250)
        self.update_score()

    def increase_score(self):
        self.clear()
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-140, 250)
        self.write(f"Score : {self.score} HighScore: {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset_game(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt',  mode='w') as data:
                data.write(str(self.high_score))
        self.score = 0
        self.update_score()
