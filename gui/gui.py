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
        self.projector = Projector([Vector(100, 0), Vector(-35, 60), Vector(0, 100), Vector(-58, -58)])

        self.projector.models.append(create_cube(50, 4, position=Vector(50, 50, 50, 50)))
        self.update()

        self.displayer.pack()

        self.__root.bind('<Button-1>', self.on_button1)

    def on_button1(self, event):
        self.projector.models[0].rotate(0, 1, math.pi / 16)
        print("\n\n" + "\n".join(str(l) for l in self.projector.models[0].lines))
        self.update()

    def update(self):
        self.displayer.delete(ALL)
        for line in self.projector.get_vision(51):
            self.displayer.draw_line(line)

    def mainloop(self):
        self.__root.mainloop()