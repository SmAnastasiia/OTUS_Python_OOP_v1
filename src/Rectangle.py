from src.Figure import Figure

class Rectangle(Figure):
    def __init__(self, side_a, side_b):
        super().__init__()
        if not isinstance(side_a, (int, float)):
            raise ValueError("Side must be a number")
        if not isinstance(side_b, (int, float)):
            raise ValueError("Side must be a number")
        if side_a <= 0 or side_b <= 0:
            raise ValueError("Can't create Rectangle")
        self.side_a = side_a
        self.side_b = side_b
        self.name = f"Rectangle {side_a} and {side_b}"

    @property
    def get_area(self):
        return self.side_a * self.side_b

    @property
    def get_perimeter(self):
        return 2 * (self.side_a + self.side_b)
