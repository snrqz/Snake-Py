from Globals import *
from GUI import *
import pygame
import sys

class Snake:
    def __init__(self):
        self.segments = [((SCREEN_WIDTH) // 2, (SCREEN_HEIGHT) // 2)]
        self.direction = 'RIGHT'

    def get_segments(self):
        return self.segments

    def check_collision(self):
        for location in self.segments:
            return location[0][0] == SCREEN_WIDTH or 0 or location[0][1] == SCREEN_HEIGHT or 0

    def move(self):
        x_position = self.segments[0][0]
        y_position = self.segments[0][1]
        if self.direction == 'UP':
            y_position -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            y_position += BLOCK_SIZE
        elif self.direction == 'LEFT':
            x_position -= BLOCK_SIZE
        else:
            x_position += BLOCK_SIZE
        self.segments.insert(0, (x_position, y_position))
        self.segments.pop()


    def grow(self):
        x_position = self.segments[0][0]
        y_position = self.segments[0][1]
        if self.direction == 'UP':
            y_position -= BLOCK_SIZE
        elif self.direction == 'DOWN':
            y_position += BLOCK_SIZE
        elif self.direction == 'LEFT':
            x_position -= BLOCK_SIZE
        else:
            x_position += BLOCK_SIZE
        self.segments.insert(0, (x_position, y_position))
        #self.segments.append((self.segments[-1][0] + BLOCK_SIZE, self.segments[-1][1]))

    def border(self):
        if (self.get_segments()[0][0] < 0 or self.get_segments()[0][1] < 0 or self.get_segments()[0][0] > SCREEN_WIDTH or self.get_segments()[0][1] > SCREEN_HEIGHT):
            sys.exit()
            pygame.quit()

    def valid(self):
        for i in range(1, len(self.segments)):
            if self.segments[0] == self.segments[i]:
                sys.exit()
                pygame.quit()
