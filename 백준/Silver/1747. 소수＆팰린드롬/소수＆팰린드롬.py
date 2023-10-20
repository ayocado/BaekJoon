import sys

N = int(sys.stdin.readline())

def prime(x):
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True

while True:
    if N == 1:
        N += 1
        continue

    if str(N) == str(N)[::-1] and prime(N):
        break
    else:
        N += 1

print(N)
