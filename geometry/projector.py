from functools import reduce

from geometry.line import Line
from geometry.primitive import Primitive


class Projector:
    models = []

    def get_vision(self, d):
        result = []
        for p in sum([m.get_final_primitives() for m in self.models], []):
            result.append(
                Primitive(
                    Line(
                        p.line.vectors[0][:2]
                        * reduce(lambda x, y: x * d / (y + d), p.line.vectors[0].coordinates[2:], 1),
                        p.line.vectors[1][:2]
                        * reduce(lambda x, y: x * d / (y + d), p.line.vectors[1].coordinates[2:], 1)
                    ),
                    color=p.color,
                    arrow=p.arrow
                )
            )
        return result

