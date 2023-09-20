from src.Rectangle import Rectangle
from src.Triangle import Triangle
from src.Square import Square
from src.Circle import Circle

import pytest


@pytest.mark.parametrize(("side_a", "side_b", "area", "perimeter"),
                         [(4, 6, 24, 20),
                          (5, 10, 50, 30)])
def test_rectangle(side_a, side_b, area, perimeter):
    r = Rectangle(side_a, side_b)
    assert r.name == f"Rectangle {side_a} and {side_b}"
    assert r.get_area == area
    assert r.get_perimeter == perimeter


@pytest.mark.parametrize(("side_a", "side_b"),
                         [(-4, -6),
                          (0, 0),
                          ('a', 0)])
def test_rectangle_negative(side_a, side_b):
    with pytest.raises(ValueError) as e:
        r = Rectangle(side_a, side_b)
        assert r.name == f"Rectangle {side_a} and {side_b}"
    if not isinstance(side_a, (int, float)):
        assert f"Side must be a number" == str(e.value)
    else:
        assert f"Can't create Rectangle" == str(e.value)


@pytest.mark.parametrize(("side", "area", "perimeter"),
                         [(4, 8, 16),
                          (5, 10, 20)])
def test_square(side, area, perimeter):
    r = Square(side)
    assert r.name == f"Square {side}"
    assert r.get_area == area
    assert r.get_perimeter == perimeter

@pytest.mark.parametrize(("side"),
                         [-4, 0, 'a'])
def test_square_negative(side):
    with pytest.raises(ValueError) as e:
        r = Square(side)
        assert r.name == f"Square {side}"
    if not isinstance(side, (int, float)):
        assert f"Side must be a number" == str(e.value)
    else:
        assert f"Can't create Square" == str(e.value)


@pytest.mark.parametrize(("side_a", "side_b", "side_c", "area", "perimeter"),
                             [(4, 4, 4, 6.93, 12), #проверка равностороннего треугольника
                              (3, 4, 5, 6, 12), #проверка тупоугольного треугольника
                              (66, 67, 68, 1942.93, 201), #проверка остроугольного треугольника
                              (3, 3, 5, 4.15, 11), #проверка равнобедренного треугольника
                              (3, 4, 5, 6, 12)]) #проверка прямоугольного треугольника

def test_triangle(side_a, side_b, side_c, area, perimeter):
    r = Triangle(side_a, side_b, side_c)
    assert r.name == f"Triangle {side_a} and {side_b} and {side_c}"
    assert r.get_area == area
    assert r.get_perimeter == perimeter

@pytest.mark.parametrize(("side_a", "side_b", "side_c"),
                           [(-4, -4, -4),
                            (0, 0, 0),
                            (2, 3, 10)])
def test_triangle_negative(side_a, side_b, side_c):
    with pytest.raises(ValueError) as e:
        r = Triangle(side_a, side_b, side_c)
        assert r.name == f"Triangle {side_a} and {side_b} and {side_c}"
    if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
        assert f"Failed to meet the conditions Triangle" == str(e.value)
    else:
        assert f"Can't create Rectangle" == str(e.value)


@pytest.mark.parametrize(("radius", "area", "perimeter"),
                             [(6, 113.1, 37.7)])
def test_circle(radius, area, perimeter):
    r = Circle(radius)
    assert r.name == f"Circle {radius}"
    assert r.get_area == area
    assert r.get_perimeter == perimeter

@pytest.mark.parametrize(("radius"),
                         [(-6),
                         ('a')])
def test_circle_negative(radius):
    with pytest.raises(ValueError) as e:
        r = Circle(radius)
        assert r.name == f"Circle {radius}"
    if not isinstance(radius, (int, float)):
        assert f"Radius must be a number" == str(e.value)
    else:
        assert f"Can't create Circle" == str(e.value)


def test_add_area():
    r = Rectangle(2, 5)
    s = Square(5)
    assert r.add_area(s) == 20


def test_add_area_negative():
    r = Rectangle(2, 5)
    c = Circle(10)
    assert c.add_area(r) != 15