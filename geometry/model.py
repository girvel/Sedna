from geometry.vector import Vector


class Model:
    def __init__(self, dimensions, lines, position=None):
        self.__lines = lines
        self.position = Vector.get_zero_vector(dimensions) if position is None else position

    @property
    def lines(self):
        return [l + self.position for l in self.__lines]

    def rotate(self, dim1, dim2, angle):
        for l in self.__lines:
            l.v1 = l.v1.rotated(dim1, dim2, angle)
            l.v2 = l.v2.rotated(dim1, dim2, angle)

