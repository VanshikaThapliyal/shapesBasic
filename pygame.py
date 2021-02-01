import pygame
WHITE=(255,255,255)
RED=(255,0,0)
GREEN=(0,255,0)
screen_size=[1000,1000]
screen=pygame.display.set_mode(screen_size)
background=screen.fill(WHITE)
pygame.draw.rect(screen,GREEN,(600,500,100,100))

keys=pygame.key.get_pressed()
if keys[pygame.K_1]==True:
    pygame.draw.rect(screen,RED,(500,500,100,100))
keep_alive=True
while keep_alive:
  pygame.display.update()
  
  
