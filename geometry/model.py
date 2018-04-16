from geometry.primitive import Primitive
from geometry.vector import Vector


class Model:
    def __init__(self, dimensions, primitives, position=None):
        self._primitives = primitives
        self.position = Vector.get_zero_vector(dimensions) if position is None else position
        self.rotation = rotation

    def get_final_primitives(self):
        return [Primitive(p.line + self.position, p.color, p.arrow) for p in self._primitives]

    def rotate(self, dim1, dim2, angle, absolute_center):
        for p in self._primitives:
            for i in range(len(p.line.vectors)):
                p.line.vectors[i] \
                    = (p.line.vectors[i] - absolute_center + self.position).rotated(dim1, dim2, angle) \
                    + absolute_center - self.position
