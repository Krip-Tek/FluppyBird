import pygame
from pygame.sprite import Sprite


class Bird(Sprite):

    def __init__(self, screen):
        super().__init__()
        self.image = pygame.image.load("image/bird.png")
        self.rect = self.image.get_rect()
        self.screen = screen
        self.screen_rect = screen.get_rect()
        self.rect.x = float(self.screen_rect.centerx) - 200
        self.rect.y = float(self.screen_rect.centery)

        self.max_speed = 10
        self.speed = 0

    def draw(self):
        self.screen.blit(self.image, self.rect)

    def move_up(self):
        if self.rect.bottom > self.screen_rect.bottom:
            self.speed = 0
        if self.rect.top > self.screen_rect.top:
            if -self.max_speed < self.speed:
                self.speed -= 0.3
            else:
                self.speed = -self.max_speed
            self.rect.y += self.speed

    def move_down(self):
        if self.rect.top < self.screen_rect.top:
            self.speed = 0
        if self.rect.bottom < self.screen_rect.bottom:
            if self.speed < self.max_speed:
                self.speed += 0.3
            else:
                self.speed = self.max_speed
            self.rect.y += self.speed
