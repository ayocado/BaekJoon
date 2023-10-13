import sys

board = [list(map(int, sys.stdin.readline().split())) for _ in range(5)]
numbers = []
for _ in range(5):
    numbers += list(map(int, sys.stdin.readline().split()))

visited = [[0] * 5 for _ in range(5)]


def bingo(board):
    cnt = 0

    for i in range(5):
        if board[i] == [1, 1, 1, 1, 1]:
            cnt += 1
        if board[0][i] and board[1][i] and board[2][i] and board[3][i] and board[4][i]:
            cnt += 1

    if board[0][0] and board[1][1] and board[2][2] and board[3][3] and board[4][4]:
        cnt += 1
    if board[0][4] and board[1][3] and board[2][2] and board[3][1] and board[4][0]:
        cnt += 1

    return cnt


flag = 0
for idx, number in enumerate(numbers):
    for row in range(5):
        for col in range(5):
            if board[row][col] == number:
                visited[row][col] = 1
                if bingo(visited) >= 3:
                    print(idx + 1)
                    flag = 1
            if flag == 1:
                break
        if flag == 1:
            break
    if flag == 1:
        break
