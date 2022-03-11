from scr.Figure import Figure


class Square(Figure):
    def __init__(self, a, name):
        super().__init__(name, 4)
        if a > 0:
            self.a = a
            self.name = name
        else:
            raise ValueError("Некорректная фигура")

    def area(self):
        return self.a ** 2

    def perimeter(self):
        return self.a * 4

    def add_area(self, figure):
        return self.area() + figure.area()
