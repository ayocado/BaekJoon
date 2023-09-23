import sys

S = sys.stdin.readline().rstrip()

# -가 있다면, 빼는 값을 최대로
# -가 없다면, 순서대로 더하기

MIN = 0
plus = 0
number = '0'
state = '+'
for s in S:
    if s == '-':
        if state == '+':
            MIN += int(number)
            state = '-'
        else:
            MIN -= int(number)
        number = ''
    elif s == '+':
        if state == '+':
            MIN += int(number)
        else:
            MIN -= int(number)
        number = ''
    else:
        number += s

if state == '-':
    MIN -= int(number)
else:
    MIN += int(number)
    
print(MIN)