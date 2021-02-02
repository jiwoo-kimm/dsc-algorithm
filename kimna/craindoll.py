def solution(board, moves):
    stack = []
    predoll, crain, doll, answer = 0, 0, 0, 0
    kind = len(board)

    for k in moves:
        crain = k - 1
        for i in range(kind):
            if  board[i][crain] != 0:
                doll = board[i][crain]
                board[i][crain] = 0
                break

        if not stack:
            stack.append(doll)
        else:
            predoll = stack.pop()
            if predoll == doll:
                answer = answer + 2
            else:
                stack.append(predoll)
                stack.append(doll)
    return answer