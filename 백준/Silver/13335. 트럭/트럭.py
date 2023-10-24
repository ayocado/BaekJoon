import sys
from collections import deque

n, w, L = map(int, sys.stdin.readline().split())
trucks = list(map(int, sys.stdin.readline().split()))
trucks.reverse()

bridge = deque([])
weight_tot = 0
answer = 0
while trucks:
    if len(bridge) == 0:
        weight = trucks.pop()
        bridge.append(weight)
        weight_tot += weight
    else:
        if len(bridge) == w:
            weight_tot -= bridge.popleft()

        if weight_tot + trucks[-1] > L:
            bridge.append(0)
        else:
            weight = trucks.pop()
            bridge.append(weight)
            weight_tot += weight

    answer += 1

print(answer + w)