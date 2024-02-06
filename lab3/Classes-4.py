import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def show(self):
        print("Coordinates: ({}, {})".format(self.x, self.y))

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def dist(self, other):
        return math.sqrt((self.x - other.x)**2 + (self.y - other.y)**2)

point1 = Point(1, 2)
point2 = Point(4, 6)
point1.show()
point2.show()
point1.move(1, 3)
point2.move(4, 6)
print("Distance between points:", point1.dist(point2))
