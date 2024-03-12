import pygame
import random
pygame.init()

#setting the runtime and height and width of the game
width=400
height=500
screen=pygame.display.set_mode([width, height])
pygame.display.set_caption('2048 Game')
timer=pygame.time.Clock()
fps=60
#draw bakground for borad
def draw_board():
    pygame.draw.rect(screen,(230,200,200,),[0,0,400,400],0,10)
    pass
def draw_pieces():
    pass
#MAIN game
run=True
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run=False
    pygame.display.flip()
pygame.quit()
