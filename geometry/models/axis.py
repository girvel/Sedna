from tkinter import LAST

from geometry.line import Line
from geometry.model import Model
from geometry.primitive import Primitive
from geometry.vector import Vector


def create_axis(dimensions, size, color, **kw):
    return Model(
        dimensions,
        [
            Primitive(
                Line(
                    Vector.get_zero_vector(dimensions),
                    Vector(*(size if i == d else 0 for i in range(dimensions)))
                ),
                color,
                arrow=LAST)
            for d in range(dimensions)
        ],
        **kw)
