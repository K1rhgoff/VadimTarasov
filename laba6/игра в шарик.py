import pygame
from pygame.draw import *
from random import randint

pygame.init()
RED = (255, 0, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
GREEN = (0, 255, 0)
MAGENTA = (255, 0, 255)
CYAN = (0, 255, 255)
BLACK = (0, 0, 0)
COLORS = [RED, BLUE, YELLOW, GREEN, MAGENTA, CYAN]
X = 0
Y = 1
R = 2
COLOR = 3
VX = 4
VY = 5

WIDTH = 1200
HEIGHT = 500

FPS = 40
screen = pygame.display.set_mode((WIDTH, HEIGHT))

number_of_circle = 10
balls = [0] * number_of_circle

def draw(ball):
    circle(screen, ball[COLOR], (ball[X], ball[Y]), ball[R])
def new_ball():

    x = randint(10, WIDTH - 50)
    y = randint(10, HEIGHT - 50)
    vx = randint(-10, 10)
    vy = randint(-10, 10)
    r = randint(10, 50)
    color = COLORS[randint(0, 5)]
    circle(screen, color, (x, y), r)
    ball = [0] * 6
    ball[X] = x
    ball[Y] = y
    ball[VX] = vx
    ball[VY] = vy
    ball[R] = r
    ball[COLOR] = color
    return ball
def move_ball(ball):
    r = ball[R]
    x = ball[X]
    y = ball[Y]
    vx = ball[VX]
    vy = ball[VY]
    if x + r > WIDTH or x - r < 0:
        vx = -vx
        x += vx
        y += vy
    if y + r > HEIGHT or y - r < 0:
        vy = -vy
        x += vx
        y += vy
    else:
        x += vx
        y += vy

    ball[X] = x
    ball[Y] = y
    ball[VX] = vx
    ball[VY] = vy
    return ball
k = 0
for k in range(1):
    point_circle = 0
    time = 0

    for i, ball in enumerate(balls):
        balls[i] = new_ball()

    pygame.display.update()
    clock = pygame.time.Clock()
    print('Очки: ')
    while time < 300:
        time += 1
        clock.tick(FPS)
        for event in pygame.event.get():

            if event.type == pygame.MOUSEBUTTONDOWN:

                for i, ball in enumerate(balls):
                    x1, y1 = event.pos
                    x = ball[X]
                    y = ball[Y]
                    r = ball[R]
                    if (x - x1) ** 2 + (y - y1) ** 2 <= r ** 2:
                        balls[i] = new_ball()
                        point_circle += 1
                        print(point_circle)


        for ball in balls:
            ball = move_ball(ball)
            draw(ball)

        pygame.display.update()
        screen.fill(BLACK)


pygame.quit()