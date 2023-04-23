import pygame
import random
from pygame.sprite import Sprite
from bird import Bird

wall_spawn_point = 0


class Wall(Sprite):

    def __init__(self, screen, image_name, walls, ):
        super().__init__()
        global wall_spawn_point
        self.bird = Bird(screen)
        self.image = pygame.image.load(f'image/{image_name}.png')
        self.rect = self.image.get_rect()

        self.screen = screen
        self.screen_rect = screen.get_rect()
        if image_name == "pipe_down":
            wall_spawn_point = random.randrange(-250, 250, 20)
            self.rect.y = 484 + wall_spawn_point
        else:
            self.rect.y = -479 + wall_spawn_point
        self.rect.x = 600

        self.add(walls)

    def update(self):
        if self.rect.x >= - 65:
            self.rect.x -= 5
        else:
            self.kill()

    def draw(self):
        self.screen.blit(self.image, self.rect)
