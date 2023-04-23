import pygame
from game_manager import GameManager
from bird import Bird
from menu import Menu

pygame.init()

screen = pygame.display.set_mode((600, 800))

# Создается группа объектов Sprite
walls = pygame.sprite.Group()
# Создается объект
bird = Bird(screen)

# Создается объект
play_button = Menu(screen)
g_m = GameManager(bird, play_button)
g_m.run(screen, walls, bird)
pygame.quit()
