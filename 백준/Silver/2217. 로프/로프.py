import sys

N = int(sys.stdin.readline())
ropes = [int(sys.stdin.readline()) for _ in range(N)]
ropes.sort(reverse=True)

answer = 0
for idx, rope in enumerate(ropes):
    if answer < (idx + 1) * rope:
        answer = (idx + 1) * rope

print(answer)