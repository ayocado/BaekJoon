import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

visited = [False] * N
s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    add_before = 0
    for i in range(N):
        if add_before != lst[i]:
            add_before = lst[i]
            s.append(lst[i])
            dfs()
            s.pop()

dfs()