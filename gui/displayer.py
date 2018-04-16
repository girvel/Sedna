from tkinter import Canvas, LAST


class Displayer(Canvas):
    def __init__(self, root, size_x, size_y, *args, **kw):
        self.size_x = size_x
        self.size_y = size_y
        super(Displayer, self).__init__(root, width=self.size_x, height=self.size_y, bg="#ccc", *args, **kw)

    def create_line(self, x1, y1, x2, y2, *args, **kw):
        super(Displayer, self).create_line(
            self.size_x / 2 + x1,
            self.size_y / 2 - y1,
            self.size_x / 2 + x2,
            self.size_y / 2 - y2,
            *args, **kw)

    def draw_primitive(self, primitive):
        self.create_line(
            *(primitive.line.vectors[0] & primitive.line.vectors[1]).coordinates,
            arrow=primitive.arrow,
            fill=primitive.color)