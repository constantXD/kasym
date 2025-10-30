import pygame
import sys
import os

pygame.init()
pygame.mixer.init()

WIDTH, HEIGHT = 400, 200
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Music player")

font = pygame.font.SysFont(None, 28)
clock = pygame.time.Clock()

playlist = [
    "music/track1.mp3",
    "music/track2.mp3",
    "music/track3.mp3",
]

current_index = 0
is_paused = False

def load_and_play(index):
    global is_paused
    if 0 <= index < len(playlist):
        pygame.mixer.music.load(playlist[index])
        pygame.mixer.music.play()
        is_paused = False

def draw_status():
    screen.fill((30, 30, 30))
    if len(playlist) == 0:
        text = font.render("No tracks", True, (200, 200, 200))
        screen.blit(text, (20, 80))
    else:
        name = os.path.basename(playlist[current_index])
        text = font.render(f"Track: {name}", True, (200, 200, 200))
        screen.blit(text, (20, 50))

        help1 = font.render("SPACE: play/pause | S: stop", True, (180, 180, 180))
        help2 = font.render("N: next | P: prev", True, (180, 180, 180))
        screen.blit(help1, (20, 100))
        screen.blit(help2, (20, 130))

    pygame.display.flip()

if playlist:
    load_and_play(current_index)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if pygame.mixer.music.get_busy():
                    pygame.mixer.music.pause()
                    is_paused = True
                else:
                    if is_paused:
                        pygame.mixer.music.unpause()
                        is_paused = False
                    else:
                        load_and_play(current_index)
            elif event.key == pygame.K_s:
                pygame.mixer.music.stop()
                is_paused = False
            elif event.key == pygame.K_n:
                if playlist:
                    current_index = (current_index + 1) % len(playlist)
                    load_and_play(current_index)
            elif event.key == pygame.K_p:
                if playlist:
                    current_index = (current_index - 1) % len(playlist)
                    load_and_play(current_index)

    draw_status()
    clock.tick(30)

pygame.quit()
sys.exit()
