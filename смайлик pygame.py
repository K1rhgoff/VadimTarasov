import pygame
from pygame.draw import *

pygame.init()

FPS =60
screen = pygame.display.set_mode((500, 500))
rect(screen, (200, 200, 200), (0, 0, 500, 500))
circle(screen, (255, 255, 0), (250, 250), 110)
circle(screen, (0, 0, 0), (250, 250), 110, 1)
circle(screen, (255, 50, 0), (210, 230), 25)
circle(screen, (0, 0, 0), (210, 230), 25, 1)
circle(screen, (0, 0, 0), (210, 230), 8)
circle(screen, (255, 50, 0), (290, 230), 17)
circle(screen, (0, 0, 0), (290, 230), 17, 1)
circle(screen, (0, 0, 0), (290, 230), 7)
rect(screen, (0, 0, 0), (205, 300, 85, 18))
line(screen, (0, 0, 0), (160, 160), (250, 200), 12)
line(screen, (0, 0, 0), (260, 215), (340, 180), 12)
pygame.display.update()
clock = pygame.time.Clock()
finished = False

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True

pygame.quit()