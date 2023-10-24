import sys

n = int(sys.stdin.readline())
numbers = list(map(int, sys.stdin.readline().split()))

dp = numbers[:]
for i in range(1, n):
    for j in range(0, i):
        if numbers[j] < numbers[i]:
            dp[i] = max(dp[i], dp[j] + numbers[i])

print(max(dp))