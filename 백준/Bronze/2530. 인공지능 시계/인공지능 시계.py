import sys

A, B, C = map(int, sys.stdin.readline().split())

D = int(sys.stdin.readline())

time = A * 3600 + B * 60 + C + D
time = time % 86400
hour = time // 3600
minute = (time % 3600) // 60
second = (time % 3600) % 60
print(hour, minute, second)