from turtle import Turtle, Screen
ALIGMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt", "r") as data:
            self.high_score = int(data.read())

        self.color("white")
        self.penup()
        self.goto(0, 260)
        self.hideturtle()
        self.updatescoreboard()

    def updatescoreboard(self):
        self.clear()
        self.write(f"Score = {self.score}, High Score: {self.high_score}", align=ALIGMENT,
                   font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("snake_game\data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.updatescoreboard()

    # def gameover(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGMENT, font=FONT)

    def increasescore(self):

        self.score += 1
        self.updatescoreboard()
