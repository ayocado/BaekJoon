import sys

N, K = map(int, sys.stdin.readline().split())
coins = [int(sys.stdin.readline()) for _ in range(N)]
coins.sort(reverse=True)

answer = 0
for coin in coins:
    if coin <= K:
        answer += K // coin
        K -= (K // coin) * coin

print(answer)