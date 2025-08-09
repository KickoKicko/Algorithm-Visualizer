import pygame
import sys




def visualize_list(list, maxValue):
    pygame.init()
    screen = pygame.display.set_mode((1300, 800+50))
    pygame.display.set_caption("Visualizer")
    screen.fill((0,0,0))
    for i in range(len(list)):
        pygame.draw.rect(screen,(100,100,100),((1200/maxValue)*i+50,850-((list[i]/maxValue)*800),(1200/maxValue),(list[i]/maxValue)*800))
    pygame.display.update()

    while(True):
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()

