import sys

string = list(map(str, sys.stdin.readline().rstrip()))
M = int(sys.stdin.readline().rstrip())
orders = []
for _ in range(M):
    orders.append(list(map(str, sys.stdin.readline().split())))

stack = []
for order in orders:
    if len(order) == 1:
        if order[0] == 'L':
            if len(string) == 0:
                continue
            else:
                stack.append(string.pop())
        elif order[0] == 'D':
            if len(stack) == 0:
                continue
            else:
                string.append(stack.pop())
        elif order[0] == 'B':
            if len(string) == 0:
                continue
            else:
                string.pop()
    else:
        string.append(order[1])

print(''.join(string) + ''.join(stack[::-1]))