import re


class Line:
    def __init__(self, *vectors):
        self.vectors = list(vectors)

    def __add__(self, other):
        return Line(*(other + v for v in self.vectors))

    def __str__(self):
        return str.format('{0} -> {1}', self.vectors[0], self.vectors[1])