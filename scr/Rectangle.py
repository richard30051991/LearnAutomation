from scr.Figure import Figure


class Rectangle(Figure):
    def __init__(self, a, b, name):
        super().__init__(name, 4)
        if int(a) != int(b) and int(a) > 0 and  int(b) > 0:
            self.a = a
            self.b = b
            self.name = name
        else:
            raise ValueError("Некорректная фигура")

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2

    def add_area(self, figure):
        return self.area() + figure.area()
