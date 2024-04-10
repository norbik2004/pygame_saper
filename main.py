import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
UNIT_SIZE = 50
RUNNING = True

win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Saper")
MINE_IMG = pygame.image.load("mine.png")
X, Y = 0, 0


def main():
    win.fill((255, 255, 255))
    draw_board()


def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_x // UNIT_SIZE, mouse_y // UNIT_SIZE
    return mouse_x, mouse_y


def draw_board():
    for i in range(int(WIDTH / UNIT_SIZE)):
        for j in range(int(HEIGHT / UNIT_SIZE)):
            pygame.draw.rect(win, (128, 128, 128), (X + (i * UNIT_SIZE), Y + (j * UNIT_SIZE), UNIT_SIZE, UNIT_SIZE), 1)


def generate_mines():
    all_coordinates = [(x, y) for x in range(11) for y in range(11)]
    mine_list = random.sample(all_coordinates, 55)
    print(mine_list)
    return mine_list


def check_if_clicked_mine(mines):
    x, y = get_mouse_position()
    pygame.draw.rect(win, (105, 105, 105), (x * UNIT_SIZE, y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE))
    for i in range(len(mines)):
        if mines[i][0] == x and mines[i][1] == y:
            print("mine touched at", x, y)
            win.blit(MINE_IMG, (x * UNIT_SIZE, y * UNIT_SIZE))


MINES = generate_mines()
main()


while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_if_clicked_mine(MINES)
    pygame.display.flip()


pygame.quit()
