import pygame


class Menu:
    def __init__(self, screen, ):
        self.image = pygame.image.load('image/play.png').convert_alpha()
        self.rect = self.image.get_rect()

        self.screen = screen
        self.screen_rect = screen.get_rect()

        self.rect.center = self.screen_rect.center

    def button_draw(self):
        self.screen.blit(self.image, self.rect)
