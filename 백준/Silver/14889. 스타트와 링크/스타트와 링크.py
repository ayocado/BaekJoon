import sys
from itertools import combinations

N = int(sys.stdin.readline())
S = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
all_score = 0
answer = float('inf')
team_A = list(combinations(list(range(N)), N // 2))

for i in range(N):
    all_score += sum(S[i])

for possibility in team_A:
    A_score, B_score = 0, 0
    team_B = []

    for i in range(N):
        if i not in possibility:
            team_B.append(i)

    for idx, score in enumerate(possibility):
        for j in range(idx + 1, N // 2):
            A_score += S[score][possibility[j]]
            A_score += S[possibility[j]][score]

    for idx, score in enumerate(team_B):
        for j in range(idx + 1, N // 2):
            B_score += S[score][team_B[j]]
            B_score += S[team_B[j]][score]

    if abs(A_score - B_score) < answer:
        answer = abs(A_score - B_score)

print(answer)