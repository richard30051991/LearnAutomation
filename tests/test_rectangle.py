from scr.Rectangle import Rectangle
from scr.Square import Square

a = 2
b = 5
name = "прямоугольник"
rectangle = Rectangle(a, b, name)


def test_create_class():
    assert isinstance(rectangle, Rectangle)


def test_area():
    assert rectangle.area() == 10


def test_perimeter():
    assert rectangle.perimeter() == 14


def test_sum_area():
    square = Rectangle(name="прямоугольник", a=2, b=3)
    assert (rectangle.add_area(square)) == square.area() + rectangle.area()


def test_incorrect_rectangle():
    try:
        Rectangle(name="прямоугольник", a=2, b=2)
    except ValueError as error:
        assert str(error) == str(ValueError('Некорректная фигура'))
