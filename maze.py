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
    
    def generate(self,start_pos):
        cell_list=[self.cells[start_pos[0]][start_pos[1]]]
        self.cells[start_pos[0]][start_pos[1]].possible_directions.pop(0)
        while(True):
            if(len(cell_list)==0):
                break
            current_cell = cell_list[len(cell_list)-1]
            if len(current_cell.possible_directions) == 0:
                cell_list.pop(len(cell_list)-1)
                continue
            randint = random.randrange(len(current_cell.possible_directions))
            next_direction = current_cell.possible_directions[randint]
            current_cell.possible_directions.pop(randint)

            if next_direction == Direction.RIGHT and current_cell.coordinates[0]<self.width-1:
                if len(self.cells[current_cell.coordinates[0]+1][current_cell.coordinates[1]].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.RIGHT)
                self.cells[current_cell.coordinates[0]+1][current_cell.coordinates[1]].directions.append(Direction.LEFT)
                cell_list.append(self.cells[current_cell.coordinates[0]+1][current_cell.coordinates[1]])

            elif next_direction == Direction.DOWN and current_cell.coordinates[1]<self.height-1:
                if len(self.cells[current_cell.coordinates[0]][current_cell.coordinates[1]+1].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.DOWN)
                self.cells[current_cell.coordinates[0]][current_cell.coordinates[1]+1].directions.append(Direction.UP)
                cell_list.append(self.cells[current_cell.coordinates[0]][current_cell.coordinates[1]+1])

            elif next_direction == Direction.LEFT and current_cell.coordinates[0]>0:
                if len(self.cells[current_cell.coordinates[0]-1][current_cell.coordinates[1]].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.LEFT)
                self.cells[current_cell.coordinates[0]-1][current_cell.coordinates[1]].directions.append(Direction.RIGHT)
                cell_list.append(self.cells[current_cell.coordinates[0]-1][current_cell.coordinates[1]])

            elif next_direction == Direction.UP and current_cell.coordinates[1]>0:
                if len(self.cells[current_cell.coordinates[0]][current_cell.coordinates[1]-1].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.UP)
                self.cells[current_cell.coordinates[0]][current_cell.coordinates[1]-1].directions.append(Direction.DOWN)
                cell_list.append(self.cells[current_cell.coordinates[0]][current_cell.coordinates[1]-1])



class cell:
    def __init__(self,directions,coordinates):
        self.directions=directions
        self.possible_directions=[Direction.UP,Direction.DOWN,Direction.LEFT,Direction.RIGHT]
        self.coordinates=coordinates
    
    """def possible_directions(self):
        list = []
        for d in Direction:
            if(d not in self.directions):
                list.append(d)
        return list"""
        