import pygame
import sys
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 800, 800
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mickey Clock")
CLOCK = pygame.time.Clock()

background = pygame.image.load("base_micky.jpg").convert()
background = pygame.transform.smoothscale(background, (WIDTH, HEIGHT))
minute_hand = pygame.image.load("minute.png").convert_alpha()
second_hand = pygame.image.load("second.png").convert_alpha()

CENTER = (WIDTH // 2, HEIGHT // 2 + 40)

mw, mh = minute_hand.get_size()
sw, sh = second_hand.get_size()

minute_offset = pygame.math.Vector2(100 - mw / 2, (20) - mh / 2)
second_offset = pygame.math.Vector2(5 - sw / 2, (5) - sh / 2)

def rotate_hand(image, angle, pivot, offset):
    rotated_image = pygame.transform.rotate(image, -angle)
    rotated_offset = offset.rotate(angle)
    rect = rotated_image.get_rect(center=pivot + rotated_offset)
    return rotated_image, rect

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = datetime.now()
    sec = now.second
    minute = now.minute
    sec_angle = (sec / 60) * 360
    min_angle = (minute / 60) * 360 + (sec / 60) * 6

    SCREEN.blit(background, (0, 0))
    rotated_min, rect_min = rotate_hand(minute_hand, min_angle - 90, pygame.math.Vector2(CENTER), minute_offset)
    SCREEN.blit(rotated_min, rect_min)
    rotated_sec, rect_sec = rotate_hand(second_hand, sec_angle - 90, pygame.math.Vector2(CENTER), second_offset)
    SCREEN.blit(rotated_sec, rect_sec)
    pygame.draw.circle(SCREEN, (0, 0, 0), CENTER, 10)

    pygame.display.flip()
    CLOCK.tick(30)

pygame.quit()
sys.exit()
