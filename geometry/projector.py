from functools import reduce

from geometry.line import Line
from geometry.vector import Vector

class Projector:
    models = []

    def __init__(self, axis):
        self.axis = axis

    def get_vision(self, d):
        result = []
        for l in sum([m.lines for m in self.models], []):
            result.append(
                Line(
                    l.v1[:2] * reduce(lambda x, y: x * d / (y + d), l.v1.coordinates[2:], 1),
                    l.v2[:2] * reduce(lambda x, y: x * d / (y + d), l.v2.coordinates[2:], 1)
                )
            )
        return result

