from geometry.line import Line
from geometry.model import Model
from geometry.primitive import Primitive
from geometry.vector import Vector


def create_cube(size, dimensions, color="black", **kw):
    lines = []

    for d in range(dimensions**2):
        point = Vector(*(size * (d & 2**i == 2**i) for i in range(dimensions)))

        for n in range(dimensions):
            if point.coordinates[n] == 0:
                lines.append(
                    Line(
                        point,
                        Vector(*(point.coordinates[i] if i != n else size for i in range(dimensions)))))
    return Model(dimensions, [Primitive(l, color) for l in lines], **kw)


