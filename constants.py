import numpy as np

FPS = 20
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
KERNEL = np.array([[1, 1, 1], [1, 0, 1], [1, 1, 1]])
WIDTH = 1200
HEIGHT = 900
X_DIM = 300
Y_DIM = int(X_DIM * WIDTH / HEIGHT)
