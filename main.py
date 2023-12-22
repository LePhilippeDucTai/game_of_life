import pygame
import sys

from game_of_life import GameOfLife

# Define constants
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Sample 2D matrix (replace this with your own)


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


def main():
    pygame.init()
    W, H = 1200, 900
    n = 300
    m = int(n * W / H)
    screen = pygame.display.set_mode((W, H))
    pygame.display.set_caption("Pygame Matrix Example")
    game = GameOfLife()
    game.generate_random(n, m, 0.1)
    clock = pygame.time.Clock()

    while True:
        event_quit()
        screen.fill(WHITE)
        draw_matrix(screen, game.matrix)
        game.update()
        pygame.display.flip()
        clock.tick(30)


if __name__ == "__main__":
    main()
