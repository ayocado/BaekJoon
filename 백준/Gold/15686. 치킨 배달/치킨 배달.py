import sys
from itertools import combinations

N, M = map(int, sys.stdin.readline().split())
city = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]

house, chicken = [], []
for row in range(N):
    for col in range(N):
        info = city[row][col]
        if info == 1:
            house.append((row + 1, col + 1))
        elif info == 2:
            chicken.append((row + 1, col + 1))

cases = list(combinations(chicken, M))
answer = float('inf')
for case in cases:
    tmp_tot = 0
    for h in house:
        tmp = float('inf')
        for c in case:
            if tmp > abs(h[0] - c[0]) + abs(h[1] - c[1]):
                tmp = abs(h[0] - c[0]) + abs(h[1] - c[1])
        tmp_tot += tmp
    if answer > tmp_tot:
        answer = tmp_tot

print(answer)