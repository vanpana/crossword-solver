class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return type(other) == type(self) and self.x == other.x and self.y == other.y

    def distance(self, other):
        if self.x == other.x:
            return abs(self.y - other.y)
        return abs(self.x - other.x)
