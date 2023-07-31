from turtle import Turtle

FONT = ("Courier", 20, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.update_level()

    def update_level(self):
        self.clear()
        self.penup()
        self.hideturtle()
        self.goto(-270, 250)
        self.write(f"Level: {self.level}", font=FONT)


    def level_up(self):
        self.level += 1
        self.update_level()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game Over!!!", align= "center", font=FONT)
