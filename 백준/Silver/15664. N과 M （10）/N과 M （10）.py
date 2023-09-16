import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

visited = [False] * N
s = []

def dfs(start):
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    add_before = 0
    for i in range(start, N):
        if add_before != lst[i]:
            add_before = lst[i]
            s.append(lst[i])
            dfs(i + 1)
            s.pop()

dfs(0)
