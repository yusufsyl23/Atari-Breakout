from turtle import Turtle
from zorluk import Zorluk


class Raket(Turtle,Zorluk):
    def __init__(self,zorluk_derecesi):

        Turtle.__init__(self)
        Zorluk.__init__(self,zorluk_derecesi)
        self.speed(0)
        self.shape("square")
        self.shapesize(stretch_len = self._uzunluk, stretch_wid = 1)
        self.color("white")
        self.penup()
        self.goto(0,-250)
        self._basla =  0

    def _saga_hareket(self):
        x = self.xcor()
        if (x < 600 - (12 * self._uzunluk)):
            self.setx(x + 20)
            self._basla = 1

    def _sola_hareket(self):
        x = self.xcor()
        if (x > (600 - (12 * self._uzunluk)) * -1):
            self.setx(x - 20)
            self._basla = 1

    def _dur(self):
        self._basla = 0

    
