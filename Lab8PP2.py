#racer
import pygame, sys, random, time
from pygame.locals import *

pygame.init()

FPS = 60
FramePerSec = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS = 0

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("road.png")
DISPLAYSURF = pygame.display.set_mode((400, 600))
pygame.display.set_caption("Racer - Coins")

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)
    def move(self):
        global SCORE
        self.rect.move_ip(0, SPEED)
        if self.rect.top > SCREEN_HEIGHT:
            SCORE += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((25, 25), pygame.SRCALPHA)
        pygame.draw.circle(self.image, (255, 215, 0), (12, 12), 12)
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
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:
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

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render(str(SCORE), True, BLACK)
    DISPLAYSURF.blit(scores, (10, 10))
    coin_text = font_small.render(f"Coins: {COINS}", True, BLACK)
    DISPLAYSURF.blit(coin_text, (SCREEN_WIDTH - 120, 10))

    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        if entity != P1:
            entity.move()

    for coin in pygame.sprite.spritecollide(P1, coins, True):
        COINS += 1
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('faceit.mp3').play()
        time.sleep(0.5)
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30, 250))
        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit()
        sys.exit()

    pygame.display.update()
    FramePerSec.tick(FPS)
#snake
pygame.init()

# screen and cell size
WIDTH, HEIGHT = 800, 600
CELL = 20
FPS = 10

# score and level
score = 0
level = 1

# colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# create window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("snake")

# font for text
font = pygame.font.SysFont("Verdana", 20)

# snake body as list of positions
snake = [(100, 100), (80, 100), (60, 100)]
direction = "RIGHT"

# create food in random place not on snake
def new_food():
    while True:
        x = random.randint(0, (WIDTH - CELL) // CELL) * CELL
        y = random.randint(0, (HEIGHT - CELL) // CELL) * CELL
        if (x, y) not in snake:
            return (x, y)

# first food
food = new_food()

clock = pygame.time.Clock()

while True:
    # handle events
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            # change direction with arrows
            if event.key == K_UP and direction != "DOWN":
                direction = "UP"
            if event.key == K_DOWN and direction != "UP":
                direction = "DOWN"
            if event.key == K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            if event.key == K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # get head position
    x, y = snake[0]

    # move head
    if direction == "UP":
        y -= CELL
    elif direction == "DOWN":
        y += CELL
    elif direction == "LEFT":
        x -= CELL
    elif direction == "RIGHT":
        x += CELL

    new_head = (x, y)

    # check if hit wall or itself
    if x < 0 or x >= WIDTH or y < 0 or y >= HEIGHT or new_head in snake:
        pygame.display.update()
        pygame.time.wait(1000)
        pygame.quit()
        sys.exit()

    # add new head to snake
    snake.insert(0, new_head)

    # check if eats food
    if new_head == food:
        score += 1
        # every 4 points add level and speed
        if score % 4 == 0:
            level += 1
            FPS += 3
        food = new_food()
    else:
        # remove tail if no food
        snake.pop()

    # draw everything
    screen.fill(BLACK)
    pygame.draw.rect(screen, RED, (food[0], food[1], CELL, CELL))
    for pos in snake:
        pygame.draw.rect(screen, GREEN, (pos[0], pos[1], CELL, CELL))

    # show score and level
    score_text = font.render(f"score: {score}", True, WHITE)
    level_text = font.render(f"level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    screen.blit(level_text, (WIDTH - 120, 10))

    pygame.display.update()
    clock.tick(FPS)
#paint
import pygame
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
        progress = i / distance
        x = int(start[0] + progress * dx)
        y = int(start[1] + progress * dy)
        pygame.draw.circle(screen, color, (x, y), width)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                drawing = True
                start_pos = event.pos
            elif event.button == 3:
                drawing = False
        if event.type == pygame.MOUSEBUTTONUP:
            if mode in ('rect', 'circle') and start_pos:
                end_pos = event.pos
                x, y = start_pos
                w, h = end_pos[0] - x, end_pos[1] - y
                if mode == 'rect':
                    pygame.draw.rect(screen, color, pygame.Rect(x, y, w, h), 2)
                elif mode == 'circle':
                    center = (x + w // 2, y + h // 2)
                    radius_circle = int((abs(w) + abs(h)) / 4)
                    pygame.draw.circle(screen, color, center, radius_circle, 2)
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

    if drawing and mode == 'draw':
        mouse_pos = pygame.mouse.get_pos()
        draw_line_between(screen, start_pos, mouse_pos, radius, color)
        start_pos = mouse_pos
    elif drawing and mode == 'erase':
        mouse_pos = pygame.mouse.get_pos()
        draw_line_between(screen, start_pos, mouse_pos, radius * 2, color)
        start_pos = mouse_pos

    pygame.display.flip()
    clock.tick(60)