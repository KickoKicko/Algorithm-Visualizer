import pygame
import sys
import time

ALL_COLUMN_WIDTH=1200
WIDTH_PADDING=100

class sorting_visualizer:

    def __init__(self, list):
        pygame.init()
        self.screen = pygame.display.set_mode((ALL_COLUMN_WIDTH+WIDTH_PADDING, 800+50))
        pygame.display.set_caption("Visualizer")
        self.list = list
        self.maxValue = len(list)

    def update(self, pivot=None):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        self.screen.fill((0,0,0))

        #poorly written code to adjust for all the columns and the space between them which is half the column size and should be quantitatively on less
        column_width = ALL_COLUMN_WIDTH*(1+(1/self.maxValue)*(1/3))*(1/((self.maxValue*2)))
        space_between_column_width = column_width * 2/3
        column_width = column_width * 4/3

        for i in range(len(self.list)):
            pygame.draw.rect(self.screen,(100,100,100),((column_width+space_between_column_width)*i+50,850-((self.list[i]/self.maxValue)*800),column_width,(self.list[i]/self.maxValue)*800))
            if pivot:
                if i==pivot:
                    pygame.draw.rect(self.screen,(0,0,255),((1200/self.maxValue)*i+50,850-((self.list[i]/self.maxValue)*800),(1200/self.maxValue),(self.list[i]/self.maxValue)*800))
        pygame.display.update()
        time.sleep(0.05)
    
    def display(self, seconds):
        self.update()
        time.sleep(seconds)


