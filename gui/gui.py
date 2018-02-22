from tkinter import Tk, ALL

import math

from geometry.cube import create_cube
from geometry.projector import Projector
from geometry.vector import Vector
from gui.displayer import Displayer


class MainFrame:
    def __init__(self):
        self.__root = Tk()

        self.displayer = Displayer(self.__root, 500, 500)
        self.projector = Projector()

        self.displayer.pack()

        self.__root.bind('<Button-1>', self.on_button1)

    def run(self):
        self.projector.models.append(create_cube(50, 4, position=Vector(50, 50, 50, 50), color="blue"))
        self.update()

        self.__root.mainloop()

    def on_button1(self, event):
        self.projector.models[0].rotate(0, 1, math.pi / 16)
        self.update()

    def update(self):
        self.displayer.delete(ALL)
        for line in self.projector.get_vision(51):
            self.displayer.draw_primitive(line)