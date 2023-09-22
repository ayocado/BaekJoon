import sys

N = int(sys.stdin.readline())
Ps = list(map(int, sys.stdin.readline().split()))
Ps.sort(reverse=True)

answer = 0
for idx, P in enumerate(Ps):
    answer += (idx + 1) * P

print(answer)