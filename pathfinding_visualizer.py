from maze import maze,cell,Direction
import pygame
import sys
import time
import random


ALL_COLUMN_WIDTH=1200
WIDTH_PADDING=100

class pathfinding_visualizer:


    def __init__(self, maze):
        self.maze=maze
        pygame.init()
        self.screen = pygame.display.set_mode((1000+30, 1000+30))
        pygame.display.set_caption("Visualizer")
    
    def display_whole_maze(self):
        for i in range(self.maze.width):
            for j in range(self.maze.height):
                pygame.draw.rect(self.screen,(255,255,255),(10+i*60,10+j*60,50,50))
                self.display_cell_walls(self.maze.cells[i][j])
        time.sleep(0.02)
        pygame.display.update()
    
    def display_cell_walls(self, cell):
        pygame.draw.rect(self.screen,(255,255,255),(10+cell.coordinates[0]*60,10+cell.coordinates[1]*60,50,50))
        for d in cell.directions:
            if d == Direction.UP:
                pygame.draw.rect(self.screen,(255,255,255),(60*cell.coordinates[0]+10,60*cell.coordinates[1],50,10))
            if d == Direction.RIGHT:
                pygame.draw.rect(self.screen,(255,255,255),(60*cell.coordinates[0]+60,60*cell.coordinates[1]+10,10,50))
            if d == Direction.DOWN:
                pygame.draw.rect(self.screen,(255,255,255),(60*cell.coordinates[0]+10,60*cell.coordinates[1]+60,50,10))
            if d == Direction.LEFT:
                pygame.draw.rect(self.screen,(255,255,255),(60*cell.coordinates[0],60*cell.coordinates[1]+10,10,50))
            


    def generate(self,start_pos):
        cell_list=[self.maze.cells[start_pos[0]][start_pos[1]]]
        self.maze.cells[start_pos[0]][start_pos[1]].possible_directions.pop(0)
        while(True):
            if(len(cell_list)==0):
                break
            current_cell = cell_list[len(cell_list)-1]
            if len(current_cell.possible_directions) == 0:
                cell_list.pop(len(cell_list)-1)
                self.display_cell_walls(current_cell)
                pygame.display.update()
                time.sleep(0.01)
                continue
            randint = random.randrange(len(current_cell.possible_directions))
            next_direction = current_cell.possible_directions[randint]
            current_cell.possible_directions.pop(randint)

            if next_direction == Direction.RIGHT and current_cell.coordinates[0]<self.maze.width-1:
                if len(self.maze.cells[current_cell.coordinates[0]+1][current_cell.coordinates[1]].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.RIGHT)
                self.maze.cells[current_cell.coordinates[0]+1][current_cell.coordinates[1]].directions.append(Direction.LEFT)
                cell_list.append(self.maze.cells[current_cell.coordinates[0]+1][current_cell.coordinates[1]])

            elif next_direction == Direction.DOWN and current_cell.coordinates[1]<self.maze.height-1:
                if len(self.maze.cells[current_cell.coordinates[0]][current_cell.coordinates[1]+1].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.DOWN)
                self.maze.cells[current_cell.coordinates[0]][current_cell.coordinates[1]+1].directions.append(Direction.UP)
                cell_list.append(self.maze.cells[current_cell.coordinates[0]][current_cell.coordinates[1]+1])

            elif next_direction == Direction.LEFT and current_cell.coordinates[0]>0:
                if len(self.maze.cells[current_cell.coordinates[0]-1][current_cell.coordinates[1]].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.LEFT)
                self.maze.cells[current_cell.coordinates[0]-1][current_cell.coordinates[1]].directions.append(Direction.RIGHT)
                cell_list.append(self.maze.cells[current_cell.coordinates[0]-1][current_cell.coordinates[1]])

            elif next_direction == Direction.UP and current_cell.coordinates[1]>0:
                if len(self.maze.cells[current_cell.coordinates[0]][current_cell.coordinates[1]-1].possible_directions) != 4:
                    continue
                current_cell.directions.append(Direction.UP)
                self.maze.cells[current_cell.coordinates[0]][current_cell.coordinates[1]-1].directions.append(Direction.DOWN)
                cell_list.append(self.maze.cells[current_cell.coordinates[0]][current_cell.coordinates[1]-1])
            self.display_cell_walls(current_cell)
            pygame.display.update()
            time.sleep(0.01)
