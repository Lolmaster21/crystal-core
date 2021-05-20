import pygame
import time

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((800,800))

def PlayIntro():
  font = pygame.font.SysFont('calibri.ttf',38)
  #this fades the first sentence from white to black
  for x in range(238):
    screen.fill((238,130,238))
    text = font.render('Welcome to Lucid Crystalline ', True, (255-x,255-x,255-x), (238,130,238))
    screen.blit(text, (100,100))
    pygame.display.flip()
    time.sleep(15 / 1000)
#this fades the second sentence from white to black
  for x in range(238):
    screen.fill((238,130,238))
    text = font.render('Where you test your skills', True, (0,0,0), (238,130,238))
    text2 = font.render('IN EPIC MINI GAMES', True, (255-x,255-x,255-x), (238,130,238))
    screen.blit(text, (100,100))
    screen.blit(text2, (150,200))
    pygame.display.flip()
    time.sleep(15 / 1000)
#this fades both from black to white
  for x in range(255):
    screen.fill((238,130,238))
    text = font.render('Where you test your skills', True, (0+x,0+x,0+x), (238,130,238))
    text2 = font.render('IN EPIC MINI GAMES', True, (0+x,0+x,0+x), (238,130,238))
    screen.blit(text, (100,100))
    screen.blit(text2, (150,200))
    pygame.display.flip()
    time.sleep(15 / 1000)

