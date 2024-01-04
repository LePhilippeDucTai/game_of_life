import numpy as np
import scipy.signal as sig

from constants import KERNEL


class GameOfLife:
    def __init__(self, matrix: np.ndarray | None = None):
        self.matrix = matrix

    def generate_random(self, n, m, prob):
        self.matrix = np.random.binomial(p=prob, n=1, size=(n, m))

    def update(self):
        conv = sig.convolve(self.matrix, KERNEL, mode="same")
        self.matrix = (((self.matrix == 1) & (conv == 2)) | (conv == 3)).astype("int")


if __name__ == "__main__":
    game = GameOfLife()
    game.generate_random(50, 100, 0.3)
    game.update()
