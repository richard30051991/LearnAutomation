from scr.Rectangle import Rectangle
from scr.Circle import Circle

radius = 2
name = "Круг"
circle = Circle(radius, name)


def test_create_class():
    assert isinstance(circle, Circle)


def test_area():
    assert circle.area() == 12.566370614359172


def test_perimeter():
    assert circle.perimeter() == 12.566370614359172


def test_sum_area():
    square = Rectangle(name="прямоугольник", a=2, b=3)
    assert (circle.add_area(square)) == square.area() + circle.area()


def test_incorrect_circle():
    try:
        Circle(name="круг", radius=0)
    except ValueError as error:
        assert str(error) == str(ValueError('Некорректная фигура'))