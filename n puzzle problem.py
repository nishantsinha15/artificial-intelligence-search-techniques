import numpy as np
import math


def generate_puzzle(n):
    values = np.random.permutation([i for i in range(1,n+1)])
    dim = int(math.sqrt(n + 1))
    board = [[0 for i in range(dim)] for j in range(dim)]
    blank_i = np.random.randint(0, dim)
    blank_j = np.random.randint(0, dim)
    iter = 0
    for i in range(dim):
        for j in range(dim):
            if i == blank_i and j == blank_j:
                board[i][j] = 0
            else:
                board[i][j] = values[iter]
                iter += 1
    print(board)
    return board


generate_puzzle(8)
