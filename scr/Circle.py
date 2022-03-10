import math
from scr.Figure import Figure


class Circle(Figure):
    def __init__(self, radius, name):
        super().__init__(name, 1)
        if radius > 0:
            self.radius = radius
        else:
            raise ValueError("Некорректная фигура")

    def area(self):
        return math.pi * (self.radius**2)

    def perimeter(self):
        return 2 * math.pi * self.radius

    def add_area(self, figure):
        return self.area() + figure.area()
