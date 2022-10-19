from turtle import Turtle
ALIGN = "center"
FONT = ('Courier', 30, 'normal')



class Scoore(Turtle):
    def __init__(self):
        super(Scoore, self).__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.score_calc_l = 0
        self.score_calc_r = 0

        self.refrash_score(0, 0)

    def game_ower(self):
        self.goto(0, 0)
        self.write(f"GAME OWER", True, align=ALIGN, font=FONT)


    def refrash_score(self,l_scor_up, r_scor_up):
        self.score_calc_l += l_scor_up
        self.score_calc_r += r_scor_up
        self.clear()
        self.goto(0, 250)
        self.write(f"{self.score_calc_l}   :   {self.score_calc_r}", True, align=ALIGN ,font=FONT)
