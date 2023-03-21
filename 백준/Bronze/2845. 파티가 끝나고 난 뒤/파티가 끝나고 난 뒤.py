import sys

L, P = map(int, sys.stdin.readline().split())
news = list(map(int, sys.stdin.readline().split()))
people = L * P
print(news[0] - people, news[1] - people, news[2] - people, news[3] - people, news[4] - people, end='')