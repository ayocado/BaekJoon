import sys

N, M = map(int, sys.stdin.readline().split())
lst = list(map(int, sys.stdin.readline().split()))
lst.sort()

s = []

def dfs():
    if len(s) == M:
        print(' '.join(map(str, s)))
        return

    for i in lst:
        s.append(i)
        dfs()
        s.pop()

dfs()