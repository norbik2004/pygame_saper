import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
UNIT_SIZE = 50
RUNNING = True

win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((255, 255, 255))
pygame.display.set_caption("Saper")

X, Y = 0, 0


def main():
    for i in range(int(WIDTH / UNIT_SIZE)):
        for j in range(int(HEIGHT / UNIT_SIZE)):
            pygame.draw.rect(win, (128, 128, 128), (X + (i * UNIT_SIZE), Y + (j * UNIT_SIZE), UNIT_SIZE, UNIT_SIZE), 1)


def generate_mines():
    pass


def calculate_tile(x, y):
    x = (x // UNIT_SIZE)
    y = (y // UNIT_SIZE)
    return x, y


main()

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            mouse_x, mouse_y = calculate_tile(mouse_x, mouse_y)
            pygame.draw.rect(win, (255, 0, 0), (mouse_x * UNIT_SIZE, mouse_y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE), 4)

    pygame.display.flip()


pygame.quit()
