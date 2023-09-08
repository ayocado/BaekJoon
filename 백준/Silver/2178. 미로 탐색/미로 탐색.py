import sys
from collections import deque

N, M = map(int, sys.stdin.readline().split())
maze = [list(map(int, sys.stdin.readline().rstrip())) for _ in range(N)]

xx = [-1, 0, 1, 0]
yy = [0, 1, 0, -1]

row, col = 0, 0
queue = deque([[row, col]])

while queue:
    cur_row, cur_col = queue.popleft()

    for i in range(4):
        new_row = cur_row + xx[i]
        new_col = cur_col + yy[i]
        if 0 <= new_row < N and 0 <= new_col < M:
            if maze[new_row][new_col] == 1:
                queue.append([new_row, new_col])
                maze[new_row][new_col] = maze[cur_row][cur_col] + 1

print(maze[N-1][M-1])