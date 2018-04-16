import math
from tkinter import Tk, ALL

from geometry.models.axis import create_axis

from geometry.models.cube import create_cube
from geometry.projector import Projector
from geometry.vector import Vector
from gui.displayer import Displayer


class MainFrame:
    def __init__(self):
        self.__root = Tk()

        self.displayer = Displayer(self.__root, 1000, 1000)
        self.projector = Projector()
        self.dimensions = 4

        self.displayer.pack()

        self.__root.bind('<F1>', lambda e: self.rotate(0, 1))
        self.__root.bind('<F2>', lambda e: self.rotate(0, 2))
        self.__root.bind('<F3>', lambda e: self.rotate(0, 3))
        self.__root.bind('<F4>', lambda e: self.rotate(1, 2))
        self.__root.bind('<F5>', lambda e: self.rotate(1, 3))
        self.__root.bind('<F6>', lambda e: self.rotate(2, 3))

    def run(self):
        self.projector.models.append(
            create_cube(500, self.dimensions, position=Vector(-250, -250, 50, 10), color="blue")
        )

        self.projector.models.append(
            create_axis(self.dimensions, 200, "green", position=Vector(*[0] * self.dimensions))
        )

        self.update()

        self.__root.mainloop()

    def rotate(self, dim1, dim2):
        self.projector.models[0].rotate(dim1, dim2, math.pi / 16, Vector(0, 0, 300, 260))
        self.update()

    def update(self):
        self.displayer.delete(ALL)
        for line in self.projector.get_vision(500):
            self.displayer.draw_primitive(line)