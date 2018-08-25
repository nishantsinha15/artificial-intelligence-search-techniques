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


def a_star(board, dim):
    heap = []
    q = queue.PriorityQueue()
    q.put((f(board,dim), board))
    iter = 0
    visited = set([])
    visited.add(get_hash(board, dim))
    g = {}
    parent = {}
    g[get_hash(board, dim)] = 0
    parent[get_hash(board, dim)] = 0
    while not q.empty():
        iter += 1
        # print("Iteration ", iter)
        weight, current = q.get()

        # print('Current = ', current)
        if is_success(current, dim):
            print('Game Won in ', iter, ' iterations')
            print(current)
            return
        next_states = get_board_states(current, dim)
        for state in next_states:
            # print(state)
            if get_hash(state, dim) not in visited:
                parent[ get_hash(state, dim) ] = current
                g[ get_hash(state, dim) ] = temp = g[ get_hash(current, dim) ] + 1
                q.put((f(state, dim) + temp, state))
                visited.add(get_hash(state, dim))
    print("No solution found for ", iter, " iterations!")


def bfs(board, dim):
    q = queue.Queue()
    q.put(board)
    iter = 0
    visited = set([])
    visited.add(get_hash(board, dim))
    while not q.empty():
        iter += 1
        # print("Iteration ", iter)
        current = q.get()
        # print(current)
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
    print("No solution found for ", iter, "iterations!")


visited_dfs = set([])
flag = False


def dfs(board, dim, iter):
    global visited_dfs, flag
    if flag:
        return
    if is_success(board, dim):
        print('Game Won in ', iter, ' iterations')
        print(board)
        flag = True
        return
    visited_dfs.add(get_hash(board, dim))
    next_states = get_board_states(board, dim)
    for state in next_states:
        if get_hash(state, dim) not in visited_dfs:
            dfs(state, dim, iter + 1)


def f(board, dim):
    dic = {}
    iter = 0
    for i in range(dim):
        for j in range(dim):
            iter += 1
            dic[iter] = (i, j)
    distance = 0
    for i in range(dim):
        for j in range(dim):
            if( board[i][j] != 0):
                distance += abs(dic[board[i][j]][0] - i) + abs(dic[board[i][j]][1] - j)
    # print(distance)
    return distance


n = int(input("Enter the length "))
# n = 8
dim = int(math.sqrt(n + 1))
board = generate_puzzle(n, dim)
# board = [ [1,8,2],[0,4,3],[7,6,5] ]
print(board)
# dfs(board, dim, 1)
a_star(board, dim)
bfs(board, dim)
