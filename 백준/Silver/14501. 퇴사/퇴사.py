import sys

N = int(sys.stdin.readline())
li = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
dp = [0 for _ in range(N+1)]

for i in range(N-1, -1, -1):
    # 상담 종료일이 퇴사일을 초과하면 상담을 하지 않는다. (이전 dp값을 가져옴)
    if i + li[i][0] > N:
        dp[i] = dp[i + 1]
    # 상담을 하지 않는 경우와 상담을 하는 경우 최댓값을 dp값으로 저장한다.
    else:
        dp[i] = max(dp[i + 1], li[i][1] + dp[i + li[i][0]])

print(dp[0])