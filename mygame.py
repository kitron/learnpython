#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame, sys
from random import *

def drawFlower( xoffset,  yoffset, size):

    pygame.draw.circle(gameDisplay, white, (300 + xoffset,300 + yoffset), int(15 * size))
    pygame.draw.circle(gameDisplay, red, (300 + xoffset,260 + yoffset), int(9 * size))
    pygame.draw.circle(gameDisplay, red, (300 + xoffset,340 + yoffset),  int(9 * size))
    pygame.draw.circle(gameDisplay, red, (260 + xoffset,300 + yoffset), int(9 * size))
    pygame.draw.circle(gameDisplay, red, (340 + xoffset,300 + yoffset),  int(9 * size))

    pygame.draw.circle(gameDisplay, red, (330 + xoffset,270 + yoffset),  int(9 * size))
    pygame.draw.circle(gameDisplay, red, (330 + xoffset,330 + yoffset),  int(9 * size))
    pygame.draw.circle(gameDisplay, red, (270 + xoffset,270 + yoffset), int(9 * size))
    pygame.draw.circle(gameDisplay, red, (270 + xoffset,330 + yoffset),  int(9 * size))

    pygame.draw.line(gameDisplay, green, (300 + xoffset,355 + yoffset), (300 + xoffset,500 + yoffset))

pygame.init()
clock = pygame.time.Clock()
screen = pygame.display.set_mode((1000,1000),0,32)

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((1000,1000))
gameDisplay.fill(black)

pixAr = pygame.PixelArray(gameDisplay)

#pixAr[10][20] = green
#pygame.draw.line(gameDisplay, blue, (100,200), (300,450), 5)
#pygame.draw.rect(gameDisplay, red, (400,400,50,25))
#pygame.draw.circle(gameDisplay, white, (150,150), 75)
#pygame.draw.polygon(gameDisplay, green, ((25,75), (76, 125), (250, 375), (400, 25), (60, 540)))

xoffset = 0
yoffset = 0


while True:

    #check for events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #erase the screen
    screen.fill(black)

    #draw game

    drawFlower(xoffset, yoffset, 1 + random())

    drawFlower(xoffset+200, yoffset+200, 0.5 + random())
    drawFlower(xoffset-200, yoffset+200, 1 + random())
    drawFlower(xoffset+200, yoffset-200, 1.5 + random())

    xoffset = xoffset
    yoffset = yoffset
      
    msElapsed = clock.tick(60)

    #update screen
    pygame.display.update()


