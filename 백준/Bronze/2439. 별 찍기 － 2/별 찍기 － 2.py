import sys

N = int(sys.stdin.readline())

for i in range(1, N+1):
    if i == N:
        print(' ' * (N - i) + '*' * i, end='')
    else:
        print(' ' * (N - i) + '*' * i)