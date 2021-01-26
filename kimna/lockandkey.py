def rotation(key):
    M = len(key)
    newkey = [[0]*M for _ in range(M)]

    for i in range(M):
        for j in range(M):
            newkey[j][M-1-i] = key[i][j]
    return newkey

def check(x, y, newkey, lock):
    M = len(newkey)
    N = len(lock)
    boardsize = 2 * M + N - 2
    board = [[0] * boardsize for _ in range(boardsize)]

    count = M + N - 1

    for i in range(N):
        for j in range(N):
            board[M - 1 + i][M - 1 + j] = lock[i][j]

    for i in range(M):
        for j in range(M):
            board[x+i][y+j] += newkey[i][j]

    for i in range(N):
        for j in range(N):
            if board[M-1+i][M-1+j] != 1:
                return False
    return True

def solution(key, lock):
    M = len(key)
    N = len(lock)
    result = False
    count = M + N - 1

    for i in range(4):
        for j in range(count):
            for k in range(count):
                if check(j, k, key, lock):
                    result = True
                    break
        key = rotation(key)
    return result































