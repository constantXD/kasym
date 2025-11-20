import pygame, sys, random, time
from pygame.locals import *

pygame.init()

FPS = 60
clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 800
SPEED = 5
SCORE = 0
COINS = 0

font = pygame.font.SysFont(None, 60)
font_small = pygame.font.SysFont(None, 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("road.png")
screen = pygame.display.set_mode((600, 800))
pygame.display.set_caption("Racer")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Enemy.png"), (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
        self.base_speed = SPEED
    def move(self):
        self.rect.move_ip(0, self.base_speed + COINS * 0.2)
        if self.rect.top > SCREEN_HEIGHT:
            global SCORE
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        w = random.choice([1, 2, 3])
        self.weight = w
        size = 15 + w * 5
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 215, 0), (size // 2, size // 2), size // 2)
        self.rect = self.image.get_rect(center=(random.randint(40, SCREEN_WIDTH - 40), 0))
        self.speed = random.randint(3, 6)
    def move(self):
        self.rect.move_ip(0, self.speed)
        if self.rect.top > SCREEN_HEIGHT:
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.transform.scale(pygame.image.load("Player.png"), (90, 100))
        self.rect = self.image.get_rect()
        self.rect.center = (160, 550)
    def move(self):
        pressed = pygame.key.get_pressed()
        if pressed[K_LEFT] and self.rect.left > 0:
            self.rect.move_ip(-5, 0)
        if pressed[K_RIGHT] and self.rect.right < SCREEN_WIDTH:
            self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()
for _ in range(3):
    coins.add(Coin())

enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1, E1, *coins)

INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.3
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.blit(background, (0, 0))
    score_text = font_small.render(str(SCORE), True, BLACK)
    screen.blit(score_text, (10, 10))
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    screen.blit(coin_text, (SCREEN_WIDTH - 140, 10))

    for entity in all_sprites:
        screen.blit(entity.image, entity.rect)
        entity.move()

    for coin in pygame.sprite.spritecollide(P1, coins, True):
        COINS += coin.weight
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('faceit.mp3').play()
        time.sleep(0.5)
        screen.fill(RED)
        screen.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    clock.tick(FPS)
import pygame, sys, random, time
from pygame.locals import *

pygame.init()

WIDTH, HEIGHT = 800, 600
CELL = 20
FPS = 10

score = 0
level = 1

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")

font = pygame.font.SysFont("Verdana", 20)

snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

def new_food():
    x = random.randint(0, (WIDTH - CELL) // CELL) * CELL
    y = random.randint(0, (HEIGHT - CELL) // CELL) * CELL
    w = random.choice([1, 2, 3])
    return {"pos": (x, y), "weight": w, "time": time.time()}

food = new_food()
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    x, y = snake[0]

    if direction == "UP":
        y -= CELL
    elif direction == "DOWN":
        y += CELL
    elif direction == "LEFT":
        x -= CELL
    elif direction == "RIGHT":
        x += CELL

    new_head = (x, y)

    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake:
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.quit()
        sys.exit()

    snake.insert(0, new_head)

    if new_head == food["pos"]:
        score += food["weight"]
        if score % 4 == 0:
            level += 1
            FPS += 3
        food = new_food()
    else:
        snake.pop()

    if time.time() - food["time"] > 5:
        food = new_food()

    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (food["pos"][0], food["pos"][1], CELL, CELL))
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], CELL, CELL))

    score_text = font.render(f"score: {score}", True, WHITE)
    level_text = font.render(f"level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(FPS)

import pygame, sys
pygame.init()

screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
screen.fill((255, 255, 255))

radius = 10
color = (0, 0, 255)
mode = 'draw'
start_pos = None
drawing = False

def draw_line_between(screen, start, end, width, color):
    dx = end[0] - start[0]
    dy = end[1] - start[1]
    distance = max(abs(dx), abs(dy))
    for i in range(distance):
        p = i / distance
        x = int(start[0] + p * dx)
        y = int(start[1] + p * dy)
        pygame.draw.circle(screen, color, (x, y), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
            elif event.button == 3:
                drawing = False

        if event.type == pygame.MOUSEBUTTONUP:
            if start_pos:
                end_pos = event.pos
                x, y = start_pos
                w, h = end_pos[0] - x, end_pos[1] - y

                if mode == 'rect':
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h), 2)

                elif mode == 'square':
                    side = min(abs(w), abs(h))
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, side, side), 2)

                elif mode == 'triangle_r':
                    p1 = (x, y)
                    p2 = (x, y + h)
                    p3 = (x + w, y + h)
                    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

                elif mode == 'triangle_e':
                    cx = x + w // 2
                    p1 = (cx, y)
                    p2 = (x, y + h)
                    p3 = (x + w, y + h)
                    pygame.draw.polygon(screen, color, [p1, p2, p3], 2)

                elif mode == 'rhombus':
                    cx = x + w // 2
                    cy = y + h // 2
                    p1 = (cx, y)
                    p2 = (x, cy)
                    p3 = (cx, y + h)
                    p4 = (x + w, cy)
                    pygame.draw.polygon(screen, color, [p1, p2, p3, p4], 2)

            drawing = False
            start_pos = None

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_r:
                color = (255, 0, 0)
            elif event.key == pygame.K_g:
                color = (0, 255, 0)
            elif event.key == pygame.K_b:
                color = (0, 0, 255)
            elif event.key == pygame.K_w:
                color = (255, 255, 255)
            elif event.key == pygame.K_e:
                mode = 'erase'
                color = (255, 255, 255)
            elif event.key == pygame.K_p:
                mode = 'draw'
            elif event.key == pygame.K_c:
                mode = 'circle'
            elif event.key == pygame.K_t:
                mode = 'rect'
            elif event.key == pygame.K_s:
                mode = 'square'
            elif event.key == pygame.K_q:
                mode = 'triangle_r'
            elif event.key == pygame.K_v:
                mode = 'triangle_e'
            elif event.key == pygame.K_h:
                mode = 'rhombus'

    if drawing and mode == 'draw':
        mouse = pygame.mouse.get_pos()
        draw_line_between(screen, start_pos, mouse, radius, color)
        start_pos = mouse
    elif drawing and mode == 'erase':
        mouse = pygame.mouse.get_pos()
        draw_line_between(screen, start_pos, mouse, radius * 2, color)
        start_pos = mouse

    pygame.display.flip()
    clock.tick(60)