from scr.Figure import Figure


class Triangle(Figure):
    def __init__(self, a, b, c, name):
        super().__init__(name, 3)
        if a + b > c and b + c > a and a + c > b:
            self.a = a
            self.b = b
            self.c = c
        else:
            raise ValueError("Некорректная фигура")

    def area(self):
        p = (self.a + self.b + self.c) / 2.0
        return (p * (p - self.a) * (p - self.b) * (p - self.c)) ** 0.5

    def perimeter(self):
        return self.a + self.b + self.c

    def add_area(self, figure):
        return self.area() + figure.area()
