import pygame
import random

pygame.init()

WIDTH, HEIGHT = 500, 500
UNIT_SIZE = 50
RUNNING = True
font = pygame.font.Font(None, 70)
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
    return mine_list


def get_those_numbers(mines):
    score = 0
    for x in range(WIDTH // UNIT_SIZE):
        for y in range(WIDTH // UNIT_SIZE):
            # permutacje x i y
            for dx in range(-1, 2):
                for dy in range(-1, 2):
                    if dx == 0 and dy == 0:
                        continue
                    if (x + dx, y + dy) in mines:
                        score += 1
            if (x, y) not in mines:
                text_surface = font.render(str(score), True, (255, 255, 255))
                win.blit(text_surface, (x * UNIT_SIZE + UNIT_SIZE // 2 - text_surface.get_width() // 2, y * UNIT_SIZE + UNIT_SIZE // 2 - text_surface.get_height() // 2))
            score = 0


def check_if_clicked_mine(mines):
    x, y = get_mouse_position()
    pygame.draw.rect(win, (105, 105, 105), (x * UNIT_SIZE, y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE))
    pygame.draw.rect(win, (0, 0, 0), (x * UNIT_SIZE, y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE), 1)
    for i in range(len(mines)):
        if mines[i][0] == x and mines[i][1] == y:
            win.blit(MINE_IMG, (x * UNIT_SIZE, y * UNIT_SIZE))


MINES = generate_mines()
main()


while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            check_if_clicked_mine(MINES)
            get_those_numbers(MINES)
    pygame.display.flip()


pygame.quit()
