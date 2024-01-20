import pygame
import sys
from constants import BLACK, HEIGHT, WHITE, WIDTH


def draw_matrix(screen, matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    square_width = screen.get_width() // cols
    square_height = screen.get_height() // rows

    for row_index, row in enumerate(matrix):
        for col_index, value in enumerate(row):
            color = WHITE if value == 0 else BLACK
            pygame.draw.rect(
                screen,
                color,
                (
                    col_index * square_width,
                    row_index * square_height,
                    square_width,
                    square_height,
                ),
            )


def event_quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


def mainloop(action: callable, game, fps: int):
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Game of Life simulation")
    clock = pygame.time.Clock()
    while True:
        event_quit()
        screen.fill(WHITE)
        action(screen, game)
        pygame.display.flip()
        clock.tick(fps)
