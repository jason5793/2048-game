import pygame
import random

pygame.init()

# Setting the runtime and height and width of the game
width = 400
height = 500
screen = pygame.display.set_mode([width, height])
pygame.display.set_caption('2048 Game')
timer = pygame.time.Clock()
fps = 60
font = pygame.font.SysFont("arial.ttf", 25)

# Setting up game color
colors = {0: (204, 192, 179),
          2: (238, 238, 218),
          4: (237, 224, 200),
          8: (242, 177, 121),
          16: (245, 149, 99),
          32: (246, 124, 65),
          64: (246, 94, 59),
          128: (237, 207, 114),
          256: (237, 204, 97),
          512: (237, 200, 80),
          1024: (237, 197, 63),
          2048: (237, 194, 46),
          'light text': (249, 246, 242),
          "dark text": (119, 110, 101),
          'other': (0, 0, 0),
          'bg': (187, 173, 160)}

# Game variables initialize
board_values = [[0 for _ in range(4)] for _ in range(4)]

# Draw background for board
def draw_board():
    pygame.draw.rect(screen, colors['bg'], [0, 0, 400, 400], 0, 10)

# Draw tiles on the board
def draw_pieces(board):
    for i in range(4):
        for j in range(4):
            value = board[i][j]
            if value > 8:
                value_color = colors['light text']
            else:
                value_color = colors['dark text']
            if value <= 2048:
                color = colors[value]
            else:
                color = colors['other']
            pygame.draw.rect(screen, color, [j * 95 + 20, i * 95 + 20, 75, 75])
            if value != 0:
                text = font.render(str(value), True, value_color)
                screen.blit(text, (j * 95 + 45, i * 95 + 45))

# Generate a random tile (2 or 4) on the board
def generate_random_tile():
    empty_tiles = [(i, j) for i in range(4) for j in range(4) if board_values[i][j] == 0]
    if empty_tiles:
        tile = random.choice(empty_tiles)
        board_values[tile[0]][tile[1]] = random.choice([2, 4])

# Function to move tiles in a direction
def move(direction):
    if direction == "up":
        for j in range(4):
            column = [board_values[i][j] for i in range(4) if board_values[i][j] != 0]
            column = merge_tiles(column)
            for i in range(4):
                if i < len(column):
                    board_values[i][j] = column[i]
                else:
                    board_values[i][j] = 0
    elif direction == "down":
        for j in range(4):
            column = [board_values[i][j] for i in range(3, -1, -1) if board_values[i][j] != 0]
            column = merge_tiles(column)
            for i in range(3, -1, -1):
                if column:
                    board_values[i][j] = column.pop()
                else:
                    board_values[i][j] = 0
    elif direction == "left":
        for i in range(4):
            row = [val for val in board_values[i] if val != 0]
            row = merge_tiles(row)
            for j in range(4):
                if j < len(row):
                    board_values[i][j] = row[j]
                else:
                    board_values[i][j] = 0
    elif direction == "right":
        for i in range(4):
            row = [val for val in board_values[i] if val != 0]
            row = merge_tiles(row)
            for j in range(3, -1, -1):
                if row:
                    board_values[i][j] = row.pop()
                else:
                    board_values[i][j] = 0

# Function to merge tiles if they have the same value
def merge_tiles(row):
    for i in range(len(row) - 1):
        if row[i] == row[i + 1]:
            row[i] *= 2
            row[i + 1] = 0
    row = [val for val in row if val != 0]
    return row

# Main game loop
run = True
generate_random_tile()
while run:
    timer.tick(fps)
    screen.fill('gray')
    draw_board()
    draw_pieces(board_values)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move("up")
            elif event.key == pygame.K_DOWN:
                move("down")
            elif event.key == pygame.K_LEFT:
                move("left")
            elif event.key == pygame.K_RIGHT:
                move("right")
            generate_random_tile()
    pygame.display.flip()

pygame.quit()
