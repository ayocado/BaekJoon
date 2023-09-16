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
        if i not in s:
            if len(s) == 0:
                s.append(i)
                dfs()
                s.pop()
            else:
                if s[-1] < i:
                    s.append(i)
                    dfs()
                    s.pop()

dfs()