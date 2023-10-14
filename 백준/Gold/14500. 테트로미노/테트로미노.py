import sys

N, M = map(int, sys.stdin.readline().split())
numbers = []
for _ in range(N):
    x = list(map(int, sys.stdin.readline().split()))
    numbers.append(x)

# 기준점에서 행, 열을 이동하는 방법(19가지)
# 순서 : 하늘(2가지), 노랑(1가지), 주황(8가지), 초록(4가지), 분홍(4가지)
xx = [[1, 2, 3], [0, 0, 0], [1, 1, 0], [1, 2, 2], [0, 0, -1], [-1, -2, -2], [0, 0, 1],
            [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 0, -1], [1, 1, 2], [0, -1, -1],
            [1, 1, 2], [0, 1, 1], [0, 0, 1], [1, 2, 1], [0, 0, -1], [1, 2, 1]]
yy = [[0, 0, 0], [1, 2, 3], [0, 1, 1], [0, 0, 1], [1, 2, 2], [0, 0, -1], [-1, -2, -2],
            [0, 0, -1], [1, 2, 2], [0, 0, 1], [-1, -2, -2], [0, 1, 1], [1, 1, 2],
            [0, -1, -1], [1, 1, 2], [1, 2, 1], [0, 0, 1], [1, 2, 1], [0, 0, -1]]

add = 0   # 한 가지 테트로미노의 합
adds = [] # 모든 경우 테트로미노의 합
for row in range(N):
    for col in range(M):
        for i in range(len(xx)):
            count = 1
            add = numbers[row][col]
            for j in range(3):
                next_row = row+xx[i][j]  # 새로운 행
                next_col = col+yy[i][j]  # 새로운 열
                if 0 <= next_row < N and 0 <= next_col < M:
                    add += numbers[next_row][next_col]
                    count += 1
                else:
                    break
            if count == 4:
                adds.append(add)
print(max(adds))