import random
from Globals import *

class Food:
    def __init__(self):
        l = [i for i in range((SCREEN_HEIGHT // 2) % BLOCK_SIZE + BLOCK_SIZE, SCREEN_HEIGHT - (BLOCK_SIZE*2), BLOCK_SIZE)]
        l2 = [i for i in range((SCREEN_WIDTH // 2) % BLOCK_SIZE + BLOCK_SIZE, SCREEN_WIDTH - (BLOCK_SIZE*2), BLOCK_SIZE)]
        self.location = (l2[random.randint(0, len(l2) - 1)],l[random.randint(0, len(l) - 1)])

    def get_x(self):
        return self.location[0]

    def get_y(self):
        return self.location[1]

    def get_location(self):
        return self.location

