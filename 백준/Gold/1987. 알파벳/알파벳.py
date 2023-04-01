import sys

R, C = map(int, sys.stdin.readline().split())
board = [list(map(str, sys.stdin.readline().rstrip())) for _ in range(R)]

stack = set([(0, 0, 1, board[0][0])])
visited = [[0] * C for _ in range(R)]
visited[0][0] = 1

xx = [1, -1, 0, 0]
yy = [0, 0, 1, -1]

maxDist = 1
while stack:
    row, col, dist, alphabet = stack.pop()
    
    for i in range(4):
        newRow = row + xx[i]
        newCol = col + yy[i]
        if 0 <= newRow < R and 0 <= newCol < C:
            if board[newRow][newCol] not in alphabet:
                visited[newRow][newCol] = dist + 1
                newAlphabet = alphabet + board[newRow][newCol]
                stack.add((newRow, newCol, dist + 1, newAlphabet))
                if dist + 1 > maxDist:
                    maxDist = dist + 1

print(maxDist)