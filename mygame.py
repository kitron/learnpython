#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pygame


pygame.init()

white = (255,255,255)
black = (0,0,0)

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((800,600))
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


    pygame.draw.circle(gameDisplay, white, (300 + xoffset,300 + yoffset), 25)
    pygame.draw.circle(gameDisplay, red, (300 + xoffset,260 + yoffset), 15)
    pygame.draw.circle(gameDisplay, red, (300 + xoffset,340 + yoffset), 15)
    pygame.draw.circle(gameDisplay, red, (260 + xoffset,300 + yoffset), 15)
    pygame.draw.circle(gameDisplay, red, (340 + xoffset,300 + yoffset), 15)

    pygame.draw.circle(gameDisplay, red, (330 + xoffset,270 + yoffset), 15)
    pygame.draw.circle(gameDisplay, red, (330 + xoffset,330 + yoffset), 15)
    pygame.draw.circle(gameDisplay, red, (270 + xoffset,270 + yoffset), 15)
    pygame.draw.circle(gameDisplay, red, (270 + xoffset,330 + yoffset), 15)

    pygame.draw.line(gameDisplay, green, (300 + xoffset,355 + yoffset), (300 + xoffset,500 + yoffset))

    xoffset = xoffset + 1
    yoffset = yoffset + 1
      
      

    for event in pygame.event.get():



        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    pygame.display.update()
