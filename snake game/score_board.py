from turtle import Turtle

SCOREBOARD_COLOR = "Black"
ALIGHMENT = 'center'
FONT = ('Courier', 24, 'normal')


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color(SCOREBOARD_COLOR)
        self.penup()
        self.goto(0, 360)
        self.hideturtle()
        self.update_score()


    def update_score(self):
        self.write(arg=f"Score: {self.score}  Highest Score: {self.high_score}", move=False, align=ALIGHMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.score}")
        self.score = 0
        self.clear()
        self.update_score()
    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg="Game Over", move=False, align=ALIGHMENT, font=FONT)


    def change_score(self):
        self.score += 1
        self.clear()
        self.update_score()











