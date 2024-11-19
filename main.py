import pygame
import random
from random import *
from pygame import *
import sys


pygame.init()
surface_color = [200, 30, 150]
start_color = [255, 0, 0]

width, height = 950, 800
level_layout = [
    [3, 2, 2, 2, 2],
    [2, 1, 0, 1, 2],
    [2, 0, 1, 0, 2],
    [2, 1, 0, 1, 2],
    [2, 2, 2, 2, 2]
]

# ko ma not vse nicle razen tm k je player
# 2x klices draw level ampak spremenis input





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
character_img = pygame.image.load("nurek.png")
character_img = transform.scale(character_img, (tile_size, tile_size))



def changColor(image, color):
    colouredImage = pygame.Surface(image.get_size())
    colouredImage.fill(color)
    
    finalImage = image.copy()
    finalImage.blit(colouredImage, (0, 0), special_flags = pygame.BLEND_MULT)
    return finalImage

def draw_line(start_pos, end_pos, surface, width, color):
    pygame.draw.line(surface, color, start_pos, end_pos, width)




def draw_floor(x, y):
    screen.blit(changColor(floor_img, surface_color), (x, y))

def draw_start(x, y):
    screen.blit(changColor(floor_img, start_color), (x, y))

def draw_obstacle(x, y):
    screen.blit(obstacle_img, (x, y))
    screen.blit(changColor(obstacle_img, surface_color), (x, y))

def draw_character(x, y):
    screen.blit(character_img, (x, y))


def draw_level(level):
    for y in range(len(level)):
        for x in reversed(range(len(level[y]))): 
            
            k = x*xoff + y*yoff
            if level[y][x] == 1:
                draw_floor(k[0]+xStart, k[1]+yStart)
            elif level[y][x] == 2:
                draw_obstacle(k[0]+xStart, k[1]+yStart) 
            elif level[y][x] == 3:
                draw_start(k[0]+xStart, k[1]+yStart)
                draw_character(k[0]+xStart, k[1]+yStart)
                


def draw_backround():
    for i in range(6):
        draw_line((width, -200-200*i+move_line), (-100, 0-200*i+move_line), screen, 80, (26,26,26))
     

 
fps = 1000
fpsClock = pygame.time.Clock()

screen = pygame.display.set_mode((width, height))

move_line = 800
player_pos = [0, 0]

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill((30, 30, 30))
    
    # draw_line((width, -200+y), (0, 0+y), screen, 80, (10,10,10))
    draw_backround()
    
    draw_level(level_layout)

    # draw_character(300, 500)
    key_pressed = pygame.key.get_pressed()
    if key_pressed[K_RIGHT]:
        player_pos[0] += 1
        print(player_pos)

    move_line += 5
    if move_line == 1000:
        move_line = 800
    pygame.display.update()
    fpsClock.tick(fps)
    fpsClock.get_fps()