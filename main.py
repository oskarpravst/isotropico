import pygame
from pygame import *
import sys


pygame.init()

level_layout = [[0, 0, 0],[0,0,0],[0,0,0],[0],[0,0,0,0]]
tile_size = 128
xStart = 0
yStart = 128
xoff = pygame.math.Vector2(tile_size/2, tile_size/-4)
yoff = pygame.math.Vector2(tile_size/2, tile_size/4)



floor_img = pygame.image.load("floor.png")
floor_img = transform.scale(floor_img, (tile_size, tile_size))




def draw_tile(x, y):
    screen.blit(floor_img, (x, y))



def draw_level(level):
    for y in range(len(level)):
        for x in reversed(range(len(level[y]))):

            k = x*xoff + y*yoff
            draw_tile(k[0]+xStart, k[1]+yStart)
    

 
fps = 60
fpsClock = pygame.time.Clock()
width, height = 950, 800
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