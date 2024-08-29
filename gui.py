import pygame
from Snake import *
from Food import *
from Globals import *
import sys

def init_screen():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Snake")

    return screen

def end_game():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def draw_snake(snake: Snake, screen):
    for segment in snake.get_segments():
        pygame.draw.rect(screen, GREEN,  (segment[0], segment[1],
                                          BLOCK_SIZE, BLOCK_SIZE))


def draw_food(food:Food, screen, color):
    pygame.draw.rect(screen, color,  (food.get_x(), food.get_y(), BLOCK_SIZE, BLOCK_SIZE))

def choose_color():
    return COLOR_ARR[(random.randint(0, len(COLOR_ARR)-1))]

def snake_eat(snake:Snake, food:Food):
    return food.get_location() == snake.get_segments()[0]

def EXE():
    pygame.quit()
    sys.exit()

def handle_events(snake):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if snake.direction == "DOWN":
                    EXE()
                else:
                    snake.direction = "UP"
            elif event.key == pygame.K_DOWN:
                if snake.direction == "UP":
                    EXE()
                else:
                    snake.direction = "DOWN"
            elif event.key == pygame.K_LEFT:
                if snake.direction == 'RIGHT':
                    EXE()
                else:
                    snake.direction = "LEFT"
            elif event.key == pygame.K_RIGHT:
                if snake.direction == 'LEFT':
                    EXE()
                else:
                    snake.direction = "RIGHT"



