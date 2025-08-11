from maze import maze,cell,Direction

import pygame
import sys
import time

ALL_COLUMN_WIDTH=1200
WIDTH_PADDING=100

class pathfinding_visualizer:


    def __init__(self, maze):
        self.maze=maze
        pygame.init()
        self.screen = pygame.display.set_mode((1000+30, 1000+30))
        pygame.display.set_caption("Visualizer")
    
    def display_maze(self):
        for i in range(self.maze.width):
            for j in range(self.maze.height):
                pygame.draw.rect(self.screen,(255,255,255),(10+i*60,10+j*60,50,50))
                self.display_cell_walls(self.maze.cells[i][j],60*(i+1)-40,60*(j+1)-40)
        pygame.display.update()
    
    def display_cell_walls(self, cell,xpos,ypos):
        for d in cell.directions:
            if d == Direction.UP:
                pygame.draw.rect(self.screen,(255,255,255),(xpos-10,ypos-25,50,50))
            if d == Direction.RIGHT:
                pygame.draw.rect(self.screen,(255,255,255),(xpos+15,ypos-10,50,50))
            if d == Direction.DOWN:
                pygame.draw.rect(self.screen,(255,255,255),(xpos-10,ypos,50,50))
            if d == Direction.LEFT:
                pygame.draw.rect(self.screen,(255,255,255),(xpos-15,ypos-10,50,50))
