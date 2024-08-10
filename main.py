from GUI import *
from Food import *
screen = init_screen()
snake = Snake()
food = Food()

color = choose_color()
clock = pygame.time.Clock()

while True:
    handle_events(snake)
    snake.valid()
    snake.move()

    screen.fill(BLACK)
    draw_food(food, screen, color)
    draw_snake(snake, screen)
    if snake_eat(snake, food):
        snake.grow()
        food = Food()
        color = choose_color()
    snake.border()
    pygame.display.flip()

    eval = (len(snake.segments) / 10) * 1.135
    clock.tick(SNAKE_SPEED + eval)
