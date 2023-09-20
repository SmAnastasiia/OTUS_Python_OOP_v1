from src.Figure import Figure
import math
class Triangle(Figure):
    def __init__(self, side_a, side_b, side_c):
        super().__init__()
        if side_a + side_b <= side_c or side_a + side_c <= side_b or side_b + side_c <= side_a:
            raise ValueError("Failed to meet the conditions Triangle")
        if side_a <= 0 or side_b <= 0 or side_c <= 0:
            raise ValueError("Can't create Triangle")
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.name = f"Triangle {side_a} and {side_b} and {side_c}"


    @property
    def get_area(self):
        # Вычисляем полупериметр треугольника
        s = (self.side_a + self.side_b + self.side_c) / 2

        # Вычисляем площадь треугольника по формуле Герона
        area = round(math.sqrt(s * (s - self.side_a) * (s - self.side_b) * (s - self.side_c)), 2)

        return area

    @property
    def get_perimeter(self):
        return self.side_a + self.side_b + self.side_c