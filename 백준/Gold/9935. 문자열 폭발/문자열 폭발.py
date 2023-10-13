import sys

strings = sys.stdin.readline().rstrip()
explode_str = sys.stdin.readline().rstrip()

stack = []
len_explode = len(explode_str)
for idx, string in enumerate(strings):
    stack.append(string)
    if ''.join(stack[-len_explode:]) == explode_str:
        for _ in range(len_explode):
            stack.pop()

if len(stack) == 0:
    print('FRULA')
else:
    print(''.join(stack))