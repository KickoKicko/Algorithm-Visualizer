import enum


class Direction(enum.Enum):
    UP=1
    RIGHT=2
    DOWN=3
    LEFT=4

class maze:
    def __init__(self,cells,width,height):
        self.cells = cells
        self.width = width
        self.height = height

class cell:
    def __init__(self,directions):
        self.directions=directions