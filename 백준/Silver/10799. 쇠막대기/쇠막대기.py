import sys

stacks = list(map(str, sys.stdin.readline().rstrip()))

left, right, answer = 0, 0, 0
before_left = False

for stack in stacks:
    if stack == '(':
        left += 1
        before_left = True
    else:
        right += 1
        if before_left == True:
            answer += left - right
        else:
            answer += 1
        before_left = False

print(answer)