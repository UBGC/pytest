import pygame
import sys
import random
import math

# Inicjalizacja Pygame
pygame.init()

# Stałe ekranu
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

# Tworzenie okna gry
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Moja Gra")

# Czcionka
font = pygame.font.Font(None, 74)
small_font = pygame.font.Font(None, 50)

# Teksty
title_text = font.render("Moja Gra", True, WHITE)
play_text = small_font.render("Graj", True, BLACK)
exit_text = small_font.render("Wyjdź", True, BLACK)

# Pozycje tekstów
title_rect = title_text.get_rect(center=(WIDTH // 2, HEIGHT // 4))
play_rect = pygame.Rect(WIDTH // 3, HEIGHT // 2, 200, 60)
exit_rect = pygame.Rect(WIDTH // 3, HEIGHT // 2 + 80, 200, 60)

# Pętla strony startowej
running = True
while running:
    screen.fill(BLACK)  # Tło
    screen.blit(title_text, title_rect)  # Tytuł

    # Przycisk "Graj"
    pygame.draw.rect(screen, GREEN, play_rect)
    screen.blit(play_text, play_rect.move(60, 10))

    # Przycisk "Wyjdź"
    pygame.draw.rect(screen, RED, exit_rect)
    screen.blit(exit_text, exit_rect.move(50, 10))

    # Obsługa zdarzeń
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if play_rect.collidepoint(event.pos):
                print("Start gry!")  # Tu wstaw kod uruchamiający grę
                running = False
            if exit_rect.collidepoint(event.pos):
                pygame.quit()
                sys.exit()

    pygame.display.flip()

# (Tu można dodać kod do uruchomienia gry)
pygame.quit()
input("Naciśnij Enter, aby zakończyć...")





