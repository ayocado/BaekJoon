import sys

N, S = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

visited = [False] * N
SUM = 0
cnt = 0
answer = 0

def dfs(start):
    global SUM, cnt, answer

    if SUM == S and cnt > 0:
        answer += 1

    for i in range(start, N):
        if not visited[i]:
            visited[i] = True
            cnt += 1
            SUM += lst[i]
            dfs(i + 1)
            visited[i] = False
            cnt -= 1
            SUM -= lst[i]

dfs(0)
print(answer)