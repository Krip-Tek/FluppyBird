import pygame
from wall import Wall

time_wait = 0
num_point = 0
bird_life = False
game_key = True


def pipe_spawn(screen, walls, ):
    down_wall = Wall(screen, 'pipe_down', walls, )
    Wall(screen, 'pipe_up', walls, )
    return down_wall


def screen_update():  # Обновление дисплея
    pygame.display.update()


def collision_check(walls, bird):
    global bird_life
    bird_life = True
    for wall in walls:
        if pygame.sprite.collide_mask(bird, wall):
            bird_life = False
    return bird_life


class GameManager:

    def __init__(self, bird, play_button):
        self.bird = bird
        self.p_b = play_button
        self.fps = 60  # Установка частоты кадров игры
        self.isJump = False
        self.font = pygame.font.SysFont('Times New Roman', 35)

    def event_check(self, screen, walls,):  # Проверка игровых событий
        global bird_life, game_key
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_key = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.isJump = True
                    bird_life = True
                    if not bird_life:
                        self.reload_lvl(screen, walls)
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_SPACE:
                    self.isJump = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                self.check_button_collied(mouse_x, mouse_y,)

    def check_button_collied(self, mouse_x, mouse_y,):
        global bird_life
        if self.p_b.rect.collidepoint(mouse_x, mouse_y):
            bird_life = True

    def screen_up(self, screen, walls):
        screen.fill("#7179C2")
        self.bird.draw()  # Отрисовка объектов
        walls.draw(screen)
        if not bird_life:
            self.p_b.button_draw()
        text = self.font.render(f"{num_point}", True, (95, 0, 144))
        screen.blit(text, (40, 40))
        screen_update()  # Обновление дисплея
        self.event_check(screen, walls,)

    def reload_lvl(self, screen, walls):
        global num_point
        for wall in walls:
            walls.remove(wall)
        screen_rect = screen.get_rect()
        self.bird.rect.x = float(screen_rect.centerx) - 200
        self.bird.rect.y = float(screen_rect.centery)
        num_point = 0

    def run(self, screen, walls, bird):
        global time_wait, bird_life, num_point, game_key
        clock = pygame.time.Clock()
        down_wall = pipe_spawn(screen, walls, )

        while game_key:
            while not bird_life and game_key:
                self.screen_up(screen, walls)
                if bird_life:
                    self.reload_lvl(screen, walls)

            if self.isJump:
                self.bird.move_up()  # Прыжок объекта
            else:
                self.bird.move_down()  # Падение объекта

            walls.update()

            if time_wait == 100:  # Установка частоты спавна препятствия
                down_wall = pipe_spawn(screen, walls, )
                time_wait = 0
            else:
                time_wait += 1

            # Добавление очков за прохождение препятствия
            if down_wall.rect.right == bird.rect.right:
                num_point += 1

            bird_life = collision_check(walls, self.bird)
            self.screen_up(screen, walls)
            clock.tick(self.fps)
