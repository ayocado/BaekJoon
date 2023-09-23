import sys

T = int(sys.stdin.readline())
N, stocks = [], []
for _ in range(T):
    N.append(int(sys.stdin.readline()))
    stocks.append(list(map(int, sys.stdin.readline().split())))

for stock in stocks:
    answer = 0
    MAX = stock[-1]
    for i in range(len(stock)-2, -1, -1):
        if stock[i] < MAX:
            answer += MAX - stock[i]
        else:
            MAX = stock[i]
            
    print(answer)