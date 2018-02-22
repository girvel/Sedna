import unittest
from unittest import TestCase

from geometry.cube import create_cube
from geometry.vector import Vector


class CubeTests(TestCase):
    def test_create_cube(self):
        def lines_number(d):
            return 1 if d == 1 else 2 * lines_number(d - 1) + 2**(d - 1)

        # arrange
        position = Vector(1, 1, 1, 1, 1)
        dimensions = 5

        # act
        cube = create_cube(2, dimensions, position=position)

        # assert
        self.assertEqual(cube.position, position)
        self.assertEqual(len(cube._primitives), lines_number(dimensions))


if __name__ == '__main__':
    unittest.main()