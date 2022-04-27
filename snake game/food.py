from turtle import Turtle
import random

FOOD_COLOR = ["black", "blue", "red", "coral", "orange", "green"]

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(FOOD_COLOR))
        # x_cor = random.randint(-380, 380)
        # y_cor = random.randint(-380, 380)
        # self.goto(x_cor, y_cor)
        self.refresh()


    def refresh(self):
        x_cor = random.randint(-380, 380)
        y_cor = random.randint(-380, 380)
        self.color(random.choice(FOOD_COLOR))
        self.goto(x_cor, y_cor)
