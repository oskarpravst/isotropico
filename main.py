import pygame
import random
from random import *
from pygame import *
import sys


pygame.init()
width, height = 950, 800
level_layout = [
    [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0],
    [0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0],
    [0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2],
    [2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2],
    [0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0],
    [0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 1, 1, 1, 1, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 2, 2, 2, 2, 2, 2, 0, 0, 0, 0, 0, 0, 0, 0]
]



tile_size = 64
level_width = (len(level_layout)+len(level_layout[0]))*tile_size/2
level_height = (len(level_layout)+len(level_layout[0]))*tile_size/4+tile_size


xStart = (width-level_width)/2
yStart = (height-level_height)/2 + len(level_layout[0])*tile_size/4
xoff = pygame.math.Vector2(tile_size/2, tile_size/-4)
yoff = pygame.math.Vector2(tile_size/2, tile_size/4)


random_color = []




floor_img = pygame.image.load("floor.png")
floor_img = transform.scale(floor_img, (tile_size, tile_size))
obstacle_img = pygame.image.load("obstacle.png")
obstacle_img = transform.scale(obstacle_img, (tile_size, tile_size))



def changColor(image, color):
    colouredImage = pygame.Surface(image.get_size())
    print(color)
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

def draw_backround(start_pos, end_pos, surface, width, color):
    pygame.draw.line(surface, color, start_pos, end_pos, width)


def draw_floor(x, y,surface_color):
    
    screen.blit(changColor(floor_img, surface_color), (x, y))

def draw_obstacle(x, y,surface_color):
    screen.blit(obstacle_img, (x, y))
    screen.blit(changColor(obstacle_img, surface_color), (x, y))



def draw_level(level, surface_color):
    for y in range(len(level)):
        for x in reversed(range(len(level[y]))): 
            surface_color = [randint(0, 255), randint(0, 255), randint(0, 255)]
            k = x*xoff + y*yoff
            if level[y][x] == 1:
                draw_floor(k[0]+xStart, k[1]+yStart,(surface_color[0], surface_color[1], surface_color[2]))
            elif level[y][x] == 2:
                draw_obstacle(k[0]+xStart, k[1]+yStart, (surface_color[0],surface_color[1], surface_color[2]))
    

 
fps = 60
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

y = 0

while True:
    
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))
    draw_backround((0,height+y), (width, -10+y), screen, 40, "grey")

    draw_level(level_layout, random_color)

    y += 10
    pygame.display.update()
    fpsClock.tick(fps)