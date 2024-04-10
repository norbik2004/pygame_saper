import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
UNIT_SIZE = 50
RUNNING = True

win = pygame.display.set_mode((WIDTH, HEIGHT))
win.fill((255, 255, 255))
pygame.display.set_caption("Saper")
MINE_IMG = pygame.image.load("mine.png")
X, Y = 0, 0

win.blit(MINE_IMG, (0, 0))
def main():
    generate_mines()
    for i in range(int(WIDTH / UNIT_SIZE)):
        for j in range(int(HEIGHT / UNIT_SIZE)):
            pygame.draw.rect(win, (128, 128, 128), (X + (i * UNIT_SIZE), Y + (j * UNIT_SIZE), UNIT_SIZE, UNIT_SIZE), 1)


def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_x // UNIT_SIZE, mouse_y // UNIT_SIZE
    return mouse_x, mouse_y


def generate_mines():
    mine_list = []
    for i in range(10):
        x_random = random.randint(0, 10)
        y_random = random.randint(0, 10)
        mine_list.append((x_random, y_random))
    print(mine_list)


def check_if_clicked_mine():
    x, y = get_mouse_position()
    pygame.draw.rect(win, (255, 0, 0), (x * UNIT_SIZE, y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE), 4)


main()


while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_if_clicked_mine()


    pygame.display.flip()


pygame.quit()
