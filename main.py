import pygame
from pygame import *
import sys


pygame.init()
width, height = 950, 800
level_layout = [[2, 2, 2, 2, 2],[2,1,1,1,2],[2,1,2,1,2],[2,1,1,1,2],[2,1,1,1,2], [2, 2, 2, 2, 2], [2, 2, 2, 2, 2],[2, 2, 2, 2, 2],[2, 2, 2, 2, 2],[2, 2, 2, 2, 2]]
tile_size = 128
xStart = width / len(level_layout) - tile_size*0.75
if len(level_layout) == 1:
    xStart = width / 4
yStart = 400
xoff = pygame.math.Vector2(tile_size/2, tile_size/-4)
yoff = pygame.math.Vector2(tile_size/2, tile_size/4)



floor_img = pygame.image.load("floor.png")
floor_img = transform.scale(floor_img, (tile_size, tile_size))
obstacle_img = pygame.image.load("obstacle.png")
obstacle_img = transform.scale(obstacle_img, (tile_size, tile_size))




def draw_floor(x, y):
    screen.blit(floor_img, (x, y))

def draw_obstacle(x, y):
    screen.blit(obstacle_img, (x, y))



def draw_level(level):
    for y in range(len(level)):
        for x in reversed(range(len(level[y]))): 
            
            k = x*xoff + y*yoff
            if level[y][x] == 1:
                draw_floor(k[0]+xStart, k[1]+yStart)
            elif level[y][x] == 2:
                draw_obstacle(k[0]+xStart, k[1]+yStart)
    

 
fps = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))
 
while True:
    screen.fill((30, 30, 30))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    draw_level(level_layout)

    pygame.display.update()
    fpsClock.tick(fps)