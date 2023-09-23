import sys

n, m = map(int, sys.stdin.readline().split())
cards = list(map(int, sys.stdin.readline().split()))

while m:
    cards.sort()
    SUM = cards[0] + cards[1]
    cards[0] = SUM
    cards[1] = SUM
    m -= 1

print(sum(cards))