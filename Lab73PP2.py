import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moving nall")

clock = pygame.time.Clock()
RADIUS = 25
STEP = 20

x = WIDTH // 2
y = HEIGHT // 2

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            new_x, new_y = x, y

            if event.key == pygame.K_UP:
                new_y -= STEP
            elif event.key == pygame.K_DOWN:
                new_y += STEP
            elif event.key == pygame.K_LEFT:
                new_x -= STEP
            elif event.key == pygame.K_RIGHT:
                new_x += STEP

            if RADIUS <= new_x <= WIDTH - RADIUS and RADIUS <= new_y <= HEIGHT - RADIUS:
                x, y = new_x, new_y

    screen.fill((255, 255, 255))
    pygame.draw.circle(screen, (255, 0, 0), (x, y), RADIUS)
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()
