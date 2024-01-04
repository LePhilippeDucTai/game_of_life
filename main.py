import pygame
from constants import FPS, X_DIM, Y_DIM

from game_of_life import GameOfLife
from render import draw_matrix, mainloop


def action(screen: pygame.Surface, game: GameOfLife):
    draw_matrix(screen, game.matrix)
    game.update()


def initialize_game():
    game = GameOfLife()
    game.generate_random(X_DIM, Y_DIM, 0.2)
    return game


def main():
    pygame.init()
    game = initialize_game()
    mainloop(action, game, FPS)


if __name__ == "__main__":
    main()
