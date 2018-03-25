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

    def between(self, p1, p2):
        if p1 == p2:
            return False

        if self.x == p1.x or self.x == p2.x:
            if p1.y < p2.y:
                return p1.y <= self.y <= p2.y
            return p2.y <= self.y <= p1.y

        if self.y == p1.y or self.y == p2.y:
            if p1.x < p2.x:
                return p1.x <= self.x <= p2.x
            return p2.x <= self.x <= p1.x

    def __str__(self):
        return "{0}, {1}".format(self.x, self.y)

    def __repr__(self):
        return str(self)
