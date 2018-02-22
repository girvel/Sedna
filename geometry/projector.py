from functools import reduce

from geometry.line import Line
from geometry.primitive import Primitive


class Projector:
    models = []

    def get_vision(self, d):
        result = []
        for p in sum([m.get_final_primitives for m in self.models], []):
            result.append(
                Primitive(
                    Line(
                        p.line.v1[:2] * reduce(lambda x, y: x * d / (y + d), p.line.v1.coordinates[2:], 1),
                        p.line.v2[:2] * reduce(lambda x, y: x * d / (y + d), p.line.v2.coordinates[2:], 1)
                    ),
                    p.color
                )
            )
        return result

