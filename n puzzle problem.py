import numpy as np
import math
import queue
import copy


def generate_puzzle(n, dim):
    values = np.random.permutation(n + 1)
    board = [[0 for i in range(dim)] for j in range(dim)]
    iter = 0
    for i in range(dim):
        for j in range(dim):
            board[i][j] = values[iter]
            iter += 1
    return board


def get_blank(board, dim):
    for i in range(dim):
        for j in range(dim):
            if board[i][j] == 0:
                return (i, j)


def get_board_states(board, dim):
    index = get_blank(board, dim)
    list1 = [(index[0] - 1, index[1]), (index[0], index[1] - 1), (index[0] + 1, index[1]), (index[0], index[1] + 1)]
    b = []
    for ij in list1:
        if 0 <= ij[0] < dim and 0 <= ij[1] < dim:
            b1 = copy.deepcopy(board)
            b1[index[0]][index[1]] = b1[ij[0]][ij[1]]
            b1[ij[0]][ij[1]] = 0
            b.append(b1)
    return b


def is_success(board, dim):
    iter = 0
    for i in range(dim):
        for j in range(dim):
            iter += 1
            if iter == dim * dim:
                return True
            if iter != board[i][j]:
                return False


def get_hash(board, dim):
    a = ''
    for i in board:
        for j in i:
            a = a + str(j)
    return a


def bfs(board, dim):
    q = queue.Queue()
    q.put(board)
    iter = 0
    visited = set([])
    visited.add(get_hash(board, dim))
    while not q.empty():
        iter += 1
        print("Iteration ", iter)
        current = q.get()
        print(current)
        if is_success(current, dim):
            print('Game Won in ', iter, ' iterations')
            print(current)
            return
        next_states = get_board_states(current, dim)
        for state in next_states:
            # print(state)
            if get_hash(state, dim) not in visited:
                q.put(state)
                visited.add(get_hash(state, dim))
        print("No solution found")



n = int(input("Enter the length "))
dim = int(math.sqrt(n + 1))
board = generate_puzzle(n, dim)
print(board)
bfs(board, dim)
