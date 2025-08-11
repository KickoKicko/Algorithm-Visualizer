import enum
import random


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
    def __init__(self,directions,coordinates):
        self.directions=directions
        self.possible_directions=[Direction.UP,Direction.DOWN,Direction.LEFT,Direction.RIGHT]
        self.coordinates=coordinates
        