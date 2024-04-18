import pygame
import random

pygame.init()

# Change these variables to increase game field, remember that width and height has to be dividable by 50 because of the textures
WIDTH, HEIGHT = 1900, 1050
MINES_AMOUNT = 100
UNIT_SIZE = 50

RUNNING = True
font = pygame.font.Font(None, 70)
win = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Saper")
MINE_IMG = pygame.image.load("mine.png")
FLAG_IMG = pygame.image.load("flag.png")
FLAG_LIST = []
X, Y = 0, 0


def main():
    win.fill((255, 255, 255))
    draw_board()
    get_those_numbers(MINES)


def get_mouse_position():
    mouse_x, mouse_y = pygame.mouse.get_pos()
    mouse_x, mouse_y = mouse_x // UNIT_SIZE, mouse_y // UNIT_SIZE
    return mouse_x, mouse_y


def draw_flag(flag_list):
    x, y = get_mouse_position()
    if (x, y) in flag_list:
        pygame.draw.rect(win, (255, 255, 255), (x * UNIT_SIZE, y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE))
        pygame.draw.rect(win, (128, 128, 128), (x * UNIT_SIZE, y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE), 1)
        flag_list.remove((x, y))
    else:
        draw_tile(x, y)
        win.blit(FLAG_IMG, (x * UNIT_SIZE, y * UNIT_SIZE))
        flag_list.append((x, y))


def draw_board():
    for i in range(int(WIDTH / UNIT_SIZE)):
        for j in range(int(HEIGHT / UNIT_SIZE)):
            pygame.draw.rect(win, (128, 128, 128), (X + (i * UNIT_SIZE), Y + (j * UNIT_SIZE), UNIT_SIZE, UNIT_SIZE), 1)


def draw_tile(x, y):
    pygame.draw.rect(win, (105, 105, 105), (x * UNIT_SIZE, y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE))
    pygame.draw.rect(win, (0, 0, 0), (x * UNIT_SIZE, y * UNIT_SIZE, UNIT_SIZE, UNIT_SIZE), 1)


def generate_mines():
    all_coordinates = [(x, y) for x in range(WIDTH // UNIT_SIZE) for y in range(HEIGHT // UNIT_SIZE)]
    mine_list = random.sample(all_coordinates, MINES_AMOUNT)
    return mine_list


def get_those_numbers(mines):
    score_tab = []
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
                score_tab.append((x, y, score))
                if score == 0:
                    draw_tile(x, y)
            score = 0
    return score_tab


def draw_near_zeros(score):
    for x in range(WIDTH // UNIT_SIZE):
        for y in range(HEIGHT // UNIT_SIZE):
            if (x, y, 0) in score:
                for dx in range(-1, 2):
                    for dy in range(-1, 2):
                        if (x+dx, y+dy, 0) not in score:
                            x_cords = x + dx
                            y_cords = y+dy
                            for score_one in score:
                                if x_cords == score_one[0] and y_cords == score_one[1] in score_one:
                                    draw_tile(x_cords, y_cords)
                                    text_surface = font.render(str(score_one[2]), True, (255, 255, 255))
                                    win.blit(text_surface, (
                                        (x_cords) * UNIT_SIZE + UNIT_SIZE // 2 - text_surface.get_width() // 2,
                                        (y_cords) * UNIT_SIZE + UNIT_SIZE // 2 - text_surface.get_height() // 2))


def check_if_clicked_mine(mines, score_tab):
    x, y = get_mouse_position()
    draw_tile(x, y)
    for score in score_tab:
        if score[0] == x and score[1] == y:
            if score[2] != 0:
                text_surface = font.render(str(score[2]), True, (255, 255, 255))
                win.blit(text_surface, (x * UNIT_SIZE + UNIT_SIZE // 2 - text_surface.get_width() // 2, y * UNIT_SIZE + UNIT_SIZE // 2 - text_surface.get_height() // 2))
    for i in range(len(mines)):
        if mines[i][0] == x and mines[i][1] == y:
            print("YOU LOST!")
            win.blit(MINE_IMG, (x * UNIT_SIZE, y * UNIT_SIZE))
            return False
    return True


MINES = generate_mines()
SCORE_TAB = get_those_numbers(MINES)
main()
draw_near_zeros(SCORE_TAB)

while RUNNING:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                RUNNING = check_if_clicked_mine(MINES, SCORE_TAB)
            if event.button == 3:
                draw_flag(FLAG_LIST)
    pygame.display.flip()
pygame.quit()
