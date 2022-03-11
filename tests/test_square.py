from scr.Rectangle import Rectangle
from scr.Square import Square

a = 2
name = "квадрат"
square = Square(a, name)


def test_create_class():
    assert isinstance(square, Square)


def test_area():
    assert square.area() == 4


def test_perimeter():
    assert square.perimeter() == 8


def test_sum_area():
    rectangle = Rectangle(name="прямоугольник", a=2, b=3)
    assert (square.add_area(rectangle)) == square.area() + rectangle.area()


def test_incorrect_square():
    try:
        Square(name="прямоугольник", a=0)
    except ValueError as error:
        assert str(error) == str(ValueError('Некорректная фигура'))

