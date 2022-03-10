from scr.Rectangle import Rectangle
from scr.Square import Square
from scr.Triangle import Triangle

a = 3
b = 3
c = 3
name = "треугольник"
triangle = Triangle(a, b, c, name)


def test_create_class():
    assert isinstance(triangle, Triangle)


def test_area():
    assert triangle.area() == 3.897114317029974


def test_perimeter():
    assert triangle.perimeter() == 9


def test_sum_area():
    square = Square(name="квадрат", a=2)
    assert (triangle.add_area(square)) == square.area() + triangle.area()


def test_incorrect_triangle():
    try:
        Triangle(name="Треугольник", a=2, b=2, c=-1)
    except ValueError as error:
        assert str(error) == str(ValueError('Некорректная фигура'))
