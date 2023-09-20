from src.Figure import Figure
class Square(Figure):
    def __init__(self, side):
        super().__init__()
        if type(side) == int and side <= 0:
            raise ValueError("Can't create Square")
        if not isinstance(side, (int, float)):
            raise ValueError("Side must be a number")
        self.side = side
        self.name = f"Square {side}"

    @property
    def get_area(self):
        return self.side * 2

    @property
    def get_perimeter(self):
        return self.side * 4