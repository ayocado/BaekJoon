import sys

numbers = list(map(int, sys.stdin.readline().split()))
numbers.sort()

print(numbers[0], numbers[1], numbers[2], end='')