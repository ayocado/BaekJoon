import sys

N = int(sys.stdin.readline())
minus, plus, one = [], [], []
for _ in range(N):
    num = int(sys.stdin.readline())
    if num > 1:
        plus.append(num)
    elif num == 1:
        one.append(num)
    else:
        minus.append(num)

minus.sort()
plus.sort(reverse=True)

answer = 0
if len(minus) % 2:
    for idx in range(0, len(minus) - 1, 2):
        answer += minus[idx] * minus[idx + 1]
    answer += minus[-1]
else:
    for idx in range(0, len(minus), 2):
        answer += minus[idx] * minus[idx + 1]

if len(plus) % 2:
    for idx in range(0, len(plus) - 1, 2):
        answer += plus[idx] * plus[idx + 1]
    answer += plus[-1]
else:
    for idx in range(0, len(plus), 2):
        answer += plus[idx] * plus[idx + 1]

answer += 1 * len(one)
print(answer)