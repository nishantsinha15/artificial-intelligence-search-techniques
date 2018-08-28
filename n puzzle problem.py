import sys
import time

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


def a_star(board, dim, max_cost=sys.maxsize):
    big = 0
    q = queue.PriorityQueue()
    q.put((f(board, dim), board))
    iter = 0
    visited = set([])
    visited.add(get_hash(board, dim))
    g = {}
    parent = {}
    g[get_hash(board, dim)] = 0
    parent[get_hash(board, dim)] = 0
    while not q.empty():
        if q.qsize() > big:
            big = q.qsize()
        iter += 1
        # print("Iteration ", iter)
        weight, current = q.get()

        # print('Current = ', current)
        if is_success(current, dim):
            print('Game Won in ', iter, ' iterations')
            print('Depth = ', g[get_hash(current, dim)])
            print('Buffer size = ', big)
            print(current)
            return 1, iter

        if g[get_hash(current, dim)] + 1 > max_cost:
            return 2, iter
        next_states = get_board_states(current, dim)
        for state in next_states:
            # print(state)
            if get_hash(state, dim) not in visited:
                parent[get_hash(state, dim)] = current
                g[get_hash(state, dim)] = temp = g[get_hash(current, dim)] + 1
                q.put((f(state, dim) + temp, state))
                visited.add(get_hash(state, dim))
    print("No solution found for ", iter, " iterations!")
    return 3, iter


def bfs(board, dim):
    big = 0
    q = queue.Queue()
    q.put(board)
    iter = 0
    visited = set([])
    visited.add(get_hash(board, dim))
    level = {}
    level[get_hash(board, dim)] = 0
    while not q.empty():
        if (q).qsize() > big:
            big = q.qsize()
        iter += 1
        # print("Iteration ", iter)
        current = q.get()
        # print(current)
        if is_success(current, dim):
            print('Game Won in ', iter, ' iterations')
            print('Depth  = ', level[get_hash(current, dim)])
            print('Buffer Size = ', big)
            print(current)
            return
        next_states = get_board_states(current, dim)
        for state in next_states:
            # print(state)
            if get_hash(state, dim) not in visited:
                q.put(state)
                visited.add(get_hash(state, dim))
                level[get_hash(state, dim)] = level[get_hash(current, dim)] + 1
    print("No solution found for ", iter, "iterations!")


visited_dfs = set([])
flag = False


def dfs(board, dim):
    q = []
    q.append(board)
    iter = 0
    big = 0
    visited = set([])
    visited.add(get_hash(board, dim))
    level = {}
    level[get_hash(board, dim)] = 0
    while len(q) > 0:
        if len(q) > big:
            big = len(q)
        iter += 1
        # print("Iteration ", iter)
        current = q.pop()
        # print(current)
        if is_success(current, dim):
            print('Game Won in ', iter, ' iterations')
            print('Depth  = ', level[get_hash(current, dim)])
            print('Maximum buffer size = ', big)
            print(current)
            return
        next_states = get_board_states(current, dim)
        for state in next_states:
            # print(state)
            if get_hash(state, dim) not in visited:
                q.append(state)
                visited.add(get_hash(state, dim))
                level[get_hash(state, dim)] = level[get_hash(current, dim)] + 1
    print("No solution found for ", iter, "iterations!")

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
            if (board[i][j] != 0):
                distance += abs(dic[board[i][j]][0] - i) + abs(dic[board[i][j]][1] - j)
    # print(distance)
    return distance


def ida_star(board, dim):
    iter = 0
    for cost in range(1, 500):
        print("Trying for cost = ", cost)
        ret, count = a_star(board, dim, cost)
        iter += count
        if  ret == 1 or ret == 3:
            print("Total Iterations = ",iter)
            return


def execute(board, dim):

    start = time.time()
    a_star(board, dim)
    end = time.time()
    print('A-star took = ', end - start, ' seconds')



    start = time.time()
    bfs(board, dim)
    end = time.time()
    print('BFS took = ', end-start, ' seconds')

    start = time.time()
    dfs(board, dim)
    end = time.time()
    print('DFS took = ', end - start, ' seconds')


    start = time.time()
    ida_star(board, dim)
    end = time.time()
    print('IDA-star took = ', end - start, ' seconds')

# n = int(input("Enter the length "))
n = 15
dim = int(math.sqrt(n + 1))
board = generate_puzzle(n, dim)
print(board)

execute(board, dim)
