import pygame
import random

"""
10 x 20 square grid
shapes: S, Z, I, O, J, L, T
represented in order by 0 - 6
"""

pygame.font.init()

# GLOBALS VARS
window_width = 800
window_height = 700
play_width = 300
play_height = 600
block_size = 30

top_left_x = (window_width - play_width) // 2
top_left_y = window_height - play_height

# shapes = [S, Z, I, O, J, L, T]
shape_colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0), (255, 165, 0), (0, 0, 255), (128, 0, 128)]
# index 0 - 6 represent shape

class Piece(object):
    def __init__(self, column, row, shape):
        self.x = column
        self.y = row
        self.shape = shape
        self.color = shape_colors[shapes.index(shape)]
        self.rotation = 0  # number from 0-3

def create_grid(locked_pos={}):
    grid = [[(0,0,0) for _ in range(10)] for _ in range(20)]

    # for i in range(len(grid)):
    #     for j in range(len(grid[i])):
    #         if (j, i) in locked_pos:
    #             c = locked_pos[(j,i)]
    #             grid[i][j] = c
    return grid

###############################
###### Drawing Functions ######
###############################
def draw_grid(surface, grid):
    x = top_left_x
    y = top_left_y

    for i in range(len(grid)):
        pygame.draw.line(surface, (128, 128, 128), (x, y + i*block_size), (x + play_width, y + i*block_size))
        for j in range(len(grid[i])):
            pygame.draw.line(surface, (128, 128, 128), (x + j*block_size, y),(x + j*block_size, y + play_height))

def draw_window(surface, grid, score=0, last_score=0):
    surface.fill((0, 0, 0))

    # Title
    pygame.font.init()
    font = pygame.font.SysFont('comicsans', 48)
    label = font.render('Tetris', 1, (255, 255, 255))
    surface.blit(label, (top_left_x + play_width / 2 - (label.get_width() / 2), 30))

    # Draw grid and its bounding rectangle
    draw_grid(surface, grid)
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 3)

    # Display update
    pygame.display.update()

############################
###### Main Game Loop ######
############################
def main(window):
    global grid
 
    locked_positions = {}  # (x,y):(255,0,0)
    grid = create_grid(locked_positions)
 
    # change_piece = False
    run = True
    # current_piece = get_shape()
    # next_piece = get_shape()
    # clock = pygame.time.Clock()
    # fall_time = 0
 
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
             
            # if event.type == pygame.KEYDOWN:
            #     if event.key == pygame.K_LEFT:
            #         current_piece.x -= 1
            #         if not valid_space(current_piece, grid):
            #             current_piece.x += 1
 
            #     elif event.key == pygame.K_RIGHT:
            #         current_piece.x += 1
            #         if not valid_space(current_piece, grid):
            #             current_piece.x -= 1
            #     elif event.key == pygame.K_UP:
            #         # rotate shape
            #         current_piece.rotation = current_piece.rotation + 1 % len(current_piece.shape)
            #         if not valid_space(current_piece, grid):
            #             current_piece.rotation = current_piece.rotation - 1 % len(current_piece.shape)
 
            #     if event.key == pygame.K_DOWN:
            #         # move shape down
            #         current_piece.y += 1
            #         if not valid_space(current_piece, grid):
            #             current_piece.y -= 1

        draw_window(window, grid)

window = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption('Tetris')
main(window)
