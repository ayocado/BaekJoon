import sys

N = int(sys.stdin.readline())
scores = [int(sys.stdin.readline()) for _ in range(N)]
scores = list(reversed(scores))

answer = 0
current_score = scores[0]
for i in range(N - 1):
    if scores[i + 1] >= current_score:
        answer += scores[i + 1] - current_score + 1
        current_score -= 1
    else:
        current_score = scores[i + 1]

print(answer)