import pygame
import sys


class sorting_visualizer:

    def __init__(self, list):
        pygame.init()
        self.screen = pygame.display.set_mode((1300, 800+50))
        pygame.display.set_caption("Visualizer")
        self.list = list
        self.maxValue = len(list)

    def update(self, pivot=None):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        self.screen.fill((0,0,0))
        for i in range(len(self.list)):
            pygame.draw.rect(self.screen,(100,100,100),((1200/self.maxValue)*i+50,850-((self.list[i]/self.maxValue)*800),(1200/self.maxValue),(self.list[i]/self.maxValue)*800))
            if pivot:
                if i==pivot:
                    pygame.draw.rect(self.screen,(0,0,255),((1200/self.maxValue)*i+50,850-((self.list[i]/self.maxValue)*800),(1200/self.maxValue),(self.list[i]/self.maxValue)*800))
        pygame.display.update()

