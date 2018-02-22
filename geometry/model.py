from geometry.primitive import Primitive
from geometry.vector import Vector


class Model:
    def __init__(self, dimensions, primitives, position=None):
        self.__primitives = primitives
        self.position = Vector.get_zero_vector(dimensions) if position is None else position

    def get_final_primitives(self):
        return [Primitive(p.line + self.position, p.color, p.arrow) for p in self.__primitives]

    def rotate(self, dim1, dim2, angle):
        for p in self.__primitives:
            p.line.v1 = p.line.v1.rotated(dim1, dim2, angle)
            p.line.v2 = p.line.v2.rotated(dim1, dim2, angle)

