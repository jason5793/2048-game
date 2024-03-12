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
#setting up game color 
colors={0:(204,192,179),
        2:(238,238,218),
        4:(237,224,200),
        8:(242,177,121),
        16:(245,149,99),
        32:(246,124,65),
        64:(246,94,59),
        128:(237,207,114),
        256:(237,204,97),
        512:(237,200,80),
        1024:(237,197,63),
        2048:(237,194),
        'light text':(249,246,242),
        "dark text":(119,110,101),
        'other':(0,0,0),
        'bg':(187,173,160)}
#game pieces 

#draw bakground for borad
def draw_board():
    pygame.draw.rect(screen,colors['bg'],[0,0,400,400],0,10)
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
