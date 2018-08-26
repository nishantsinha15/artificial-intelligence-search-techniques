import queue

import numpy as np


def create_board(n):
    board = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            board[i][j] = np.random.randint(0, 5)
    # print(board)
    return board


def is_success(board, dim):
    for i in range(1, dim-1):
        for j in range(0, dim):
            if board[i][j] == board[i - 1][j] or board[i][j] == board[i + 1][j]:
                return False
    for i in range(0, dim):
        for j in range(1, dim-1):
            if board[i][j] == board[i][j - 1] or board[i][j] == board[i][j + 1]:
                return False
    return True


def get_hash(board, dim):
    a = ''
    for i in board:
        for j in i:
            a = a + str(j)
    return a


def get_board_states(board, dim, index):
    next_states = []
    for i in range(dim):
        for j in range(dim):
            if i == index[0] and j == index[1]:
                continue
            b = board.copy()
            temp = b[index[0]][index[1]]
            b[index[0]][index[1]] = b[i][j]
            b[i][j] = temp
            next_states.append(b)
    return next_states


def remove_copies(a):
    b = []
    deleted = [0 for i in range(len(a))]
    for i in range(len(a)):
        if deleted[i] == 1:
            continue
        for j in range(i + 1, len(a)):
            if np.array_equal(a[i],a[j]):
                deleted[j] = 1;
    for i in range(len(a)):
        if deleted[i] == 0:
            b.append(a[i])
    return b


def f(board, dim):
    v = 0
    for i in range(1, dim-1):
        for j in range(0, dim):
            if board[i][j] == board[i - 1][j] or board[i][j] == board[i + 1][j]:
                v += 1
    for i in range(0, dim):
        for j in range(1, dim-1):
            if board[i][j] == board[i][j - 1] or board[i][j] == board[i][j + 1]:
                v += 1
    v /= 2
    v = int(v)
    return v

def a_star(board, dim):
    count = 1
    q = queue.PriorityQueue()
    q.put((f(board, dim),count, board))
    iter = 0
    visited = set([])
    visited.add(get_hash(board, dim))
    g = {}
    g[get_hash(board,dim)] = 0

    while not q.empty():
        iter += 1
        weight, garbage, current = q.get()
        if is_success(current, dim):
            print('Game Won in ', iter, ' iterations')
            # print('Depth  = ', level[get_hash(current, dim)])
            print(current)
            return
        a = []
        for i in range(dim):
            for j in range(dim):
                b = get_board_states(current, dim, (i, j))
                a = a + b
        a = remove_copies(a)
        for state in a:
            if get_hash(state, dim) not in visited:
                g[get_hash(state,dim)] = temp = g[get_hash(current,dim)] + 1
                q.put((temp + f(state, dim), count, state))
                count+=1
                visited.add(get_hash(state, dim))
    print("No solution found for ", iter, "iterations!")


def bfs(board, dim):
    q = queue.Queue()
    q.put(board)
    visited = set([])
    iter = 0
    while not q.empty():
        iter+=1
        if iter % 100 == 0:
            print('Iteration ', iter)
        current = q.get()
        if is_success(current, dim):
            print('Game Won in ', iter, ' iterations')
            # print('Depth  = ', level[get_hash(current, dim)])
            print(current)
            return
        a = []
        for i in range(dim):
            for j in range(dim):
                b = get_board_states(current, dim, (i, j))
                a = a + b
        a = remove_copies(a)
        for state in a:
            if get_hash(state, dim) not in visited:
                q.put(state)
                visited.add(get_hash(state, dim))
    print("No solution found for ", iter, "iterations!")


board = create_board(10)
print('Initial = ', board)
bfs(board, 3)
