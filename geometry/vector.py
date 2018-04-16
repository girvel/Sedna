from math import cos, sin


class Vector:
    def __init__(self, *coordinates):
        self.coordinates = list(coordinates)

    def __iter__(self):
        return iter(self.coordinates)

    def __add__(self, other):
        return Vector(*(x + other.coordinates[i] for i, x in enumerate(self.coordinates)))

    def __sub__(self, other):
        return self + -other

    def __neg__(self):
        return Vector(*(-c for c in self.coordinates))

    def __mul__(self, other):
        if isinstance(other, Vector):
            return sum(s * other[i] for s, i in enumerate(self))
        return Vector(*(x * other for x in self.coordinates))

    def __getitem__(self, item):
        if isinstance(item, slice):
            return Vector(*self.coordinates[item])
        return self.coordinates[item]

    def __and__(self, other):
        return Vector(*(self.coordinates + other.coordinates))

    def __eq__(self, other):
        return len(self.coordinates) == len(other.coordinates) \
            and all([self.coordinates[i] == other.coordinates[i] for i in range(len(self.coordinates))])

    def __str__(self):
        return str.format("{{{0}}}", "; ".join(str(c) for c in self.coordinates))

    def rotated(self, dim1, dim2, angle):
        dim1, dim2 = sorted((dim1, dim2))

        z = self.coordinates[dim1]
        t = self.coordinates[dim2]

        return Vector(*(
            self.coordinates[:dim1]
            + [z * cos(angle) - t * sin(angle)]
            + self.coordinates[dim1 + 1:dim2]
            + [z * sin(angle) + t * cos(angle)]
            + self.coordinates[dim2 + 1:]
        ))

    @staticmethod
    def get_zero_vector(dimensions_number):
        return Vector(*([0] * dimensions_number))
