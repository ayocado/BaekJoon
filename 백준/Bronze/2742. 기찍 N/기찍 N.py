import sys

N = int(sys.stdin.readline())

for i in range(N, 0, -1):
    if i == 1:
        print(i, end='')
    else:
        print(i)