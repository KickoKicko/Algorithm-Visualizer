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
    
    def generate(self,cell_pos):
        """cell_type1 = cell([Direction.RIGHT])
        cell_type2 = cell([Direction.LEFT])
        cell_type3 = cell([Direction.UP])
        cell_type4 = cell([Direction.DOWN])
        cell_types = [cell_type1,cell_type2,cell_type3,cell_type4]
        for i in range(self.width):
            for j in range(self.height):
                r =random.randint(0,len(cell_types)-1)
                self.cells[i][j] = cell_types[r]
        print()"""
        cell_list=[self.cells[cell_pos[0]][cell_pos[1]]]
        self.cells[cell_pos[0]][cell_pos[1]].possible_directions.pop(0)
        while(True):
            print(len(cell_list))
            if(len(cell_list)==0):
                print("hej")
                break
            current_cell = cell_list[len(cell_list)-1]
            if len(current_cell.possible_directions) == 0:
                cell_list.pop(len(cell_list)-1)
                continue
            randint = random.randrange(len(current_cell.possible_directions))
            next_direction = current_cell.possible_directions[randint]
            current_cell.possible_directions.pop(randint)

            if next_direction == Direction.RIGHT and cell_pos[0]<self.width-1:
                if len(self.cells[cell_pos[0]+1][cell_pos[1]].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.RIGHT)
                cell_pos = (cell_pos[0]+1,cell_pos[1])
                self.cells[cell_pos[0]][cell_pos[1]].directions.append(Direction.LEFT)
                cell_list.append(self.cells[cell_pos[0]][cell_pos[1]])
            elif next_direction == Direction.DOWN and cell_pos[1]<self.height-1:
                if len(self.cells[cell_pos[0]][cell_pos[1]+1].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.DOWN)
                cell_pos = (cell_pos[0],cell_pos[1]+1)
                self.cells[cell_pos[0]][cell_pos[1]].directions.append(Direction.UP)
                cell_list.append(self.cells[cell_pos[0]][cell_pos[1]])
            elif next_direction == Direction.LEFT and cell_pos[0]>0:
                if len(self.cells[cell_pos[0]-1][cell_pos[1]].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.LEFT)
                cell_pos = (cell_pos[0]-1,cell_pos[1])
                self.cells[cell_pos[0]][cell_pos[1]].directions.append(Direction.RIGHT)
                cell_list.append(self.cells[cell_pos[0]][cell_pos[1]])
            elif next_direction == Direction.UP and cell_pos[1]>0:
                if len(self.cells[cell_pos[0]][cell_pos[1]-1].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.UP)
                cell_pos = (cell_pos[0],cell_pos[1]-1)
                self.cells[cell_pos[0]][cell_pos[1]].directions.append(Direction.DOWN)
                cell_list.append(self.cells[cell_pos[0]][cell_pos[1]])
            #print("("+str(cell_pos[0])+","+str(cell_pos[1])+")")


class cell:
    def __init__(self,directions):
        self.directions=directions
        self.possible_directions=[Direction.UP,Direction.DOWN,Direction.LEFT,Direction.RIGHT]
    
    """def possible_directions(self):
        list = []
        for d in Direction:
            if(d not in self.directions):
                list.append(d)
        return list"""
        