import pygame
import math
import random

pygame.init()

info_obj = pygame.display.Info()
screen_width = info_obj.current_w
screen_height = info_obj.current_h

screen = pygame.display.set_mode((screen_width, screen_height), pygame.FULLSCREEN)
clock = pygame.time.Clock()
pygame.mouse.set_visible(False)
running = True

class Ball(pygame.sprite.Sprite):
    def __init__(self, num = 1):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill("white")
        self.rect = self.image.get_rect()
        self.pos = (math.floor(screen_width / 2), math.floor(screen_height / 2))
        self.rect.center = self.pos
        self.x_velocity = -10
        self.y_velocity = math.floor(random.random() * 12)
        self.num = num
        if num == 2:
            self.x_velocity = 10

    def update(self, players, screen):
        self.pos = [math.floor(self.pos[0] + self.x_velocity), math.floor(self.pos[1] + self.y_velocity)]
        self.rect.center = self.pos
        for player in players:
            if player.rect.colliderect(self.rect):
                self.x_velocity = - self.x_velocity
            if player.goal.rect.colliderect(self.rect):
                player.score += 1
                if player.num == 1:
                    self.num = 2
                else:
                    self.num = 1
                self.reset()
        if not screen.get_rect().contains(self.rect):
            self.y_velocity = - self.y_velocity

    def reset(self):
        self.pos = (math.floor(screen_width / 2), math.floor(screen_height / 2))
        self.rect.center = self.pos
        self.x_velocity = -10
        self.y_velocity = math.floor(random.random() * 12)
        if self.num == 2:
            self.x_velocity = 10

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class White_bar(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((10, 100))
        self.image.fill("white")
        self.rect = self.image.get_rect()

    def draw(self, surface):
        surface.blit(self.image, self.rect)

class Player(White_bar):
    def __init__(self, num = 1):
        super().__init__()
        mult = 1
        self.up = pygame.K_w
        self.down = pygame.K_s
        if num == 2:
            mult = 3
            self.up = pygame.K_UP
            self.down = pygame.K_DOWN
        self.pos = (math.floor(mult * screen_width / 4), math.floor(screen_height / 2))
        self.rect.center = self.pos
        self.num = num
        self.goal = Goal(num)
        self.score = 0

    def update(self, keys, screen):
        original_pos = self.pos
        if keys[self.up]:
            self.pos = [self.pos[0], self.pos[1] - 10]
            self.rect.center = self.pos
        if keys[self.down]:
            self.pos = [self.pos[0], self.pos[1] + 10]
            self.rect.center = self.pos
        if not screen.get_rect().contains(self.rect):
            self.pos = original_pos
            self.rect.center = self.pos

class Goal(pygame.sprite.Sprite):
    def __init__(self, num = 1):
        self.image = pygame.Surface((10, screen_height))
        self.image.fill((0, 0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.center = (screen_width - 5, math.floor(screen_height / 2))
        self.num = num
        if self.num == 2:
            self.rect.center = (5, math.floor(screen_height / 2))

class Scoreboard():
    def __init__(self):
        self.font = pygame.font.Font("Miracode.ttf", 32)
        self.score1 = 0
        self.score2 = 0
        self.image = self.font.render(f'{str(self.score1)}:{str(self.score2)}', True, (255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.center = (math.floor(screen_width / 2), math.floor(screen_height / 10))

    def update(self, score1, score2):
        self.score1 = score1
        self.score2 = score2
        self.image = self.font.render(f'{str(self.score1)}:{str(self.score2)}', True, (255, 255, 255))

    def draw(self, surface):
        surface.blit(self.image, self.rect)

player = Player(1)
player_2 = Player(2)
ball = Ball()
scoreboard = Scoreboard()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill("black")

    player.draw(screen)
    player_2.draw(screen)
    ball.draw(screen)
    scoreboard.draw(screen)
    player.update(pygame.key.get_pressed(), screen)
    player_2.update(pygame.key.get_pressed(), screen)
    ball.update([player, player_2], screen)
    scoreboard.update(player.score, player_2.score)

    pygame.display.flip()

    clock.tick(60) 

pygame.quit()
