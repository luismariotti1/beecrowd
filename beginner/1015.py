from cmath import sqrt

class point:
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, point2):
        return sqrt( pow((self.x - point2.x), 2) + pow((self.y - point2.y), 2))

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

point1 = point(x1, y1)
point2 = point(x2, y2)

print("{:.4f}".format(point1.distance(point2).real))