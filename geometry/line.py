class Line:
    def __init__(self, v1, v2):
        self.v1 = v1
        self.v2 = v2

    def __add__(self, other):
        return Line(other + self.v1, other + self.v2)

    def __str__(self):
        return str.format('{0} -> {1}', self.v1, self.v2)