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
    for idx, i in enumerate(lst):
        if not visited[idx] and add_before != i:
            add_before = i
            visited[idx] = True
            s.append(i)
            dfs()
            visited[idx] = False
            s.pop()

dfs()
