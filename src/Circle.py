from src.Figure import Figure
import math

class Circle(Figure):
    def __init__(self, radius):
        super().__init__()
        if type(radius) == int and radius <= 0:
            raise ValueError("Can't create Circle")
        if not isinstance(radius, (int, float)):
            raise ValueError("Radius must be a number")
        self.radius = radius
        self.name = f"Circle {radius}"

    @property
    def get_area(self):
        return round(math.pi * self.radius ** 2, 2)

    @property
    def get_perimeter(self):
        return round(2 * math.pi * self.radius, 2)