import sys

N = int(sys.stdin.readline())
lines = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
lines.sort()

tot = []
for idx, line in enumerate(lines):
    if idx == 0:
        tot.append(line)
    else:
        if tot[-1][1] == line[0]:
            tot[-1][1] = line[1]
        elif tot[-1][1] < line[0]:
            tot.append(line)
        else:
            if tot[-1][1] < line[1]:
                tot[-1][1] = line[1]
            else:
                continue
answer = 0
for t in tot:
    answer += t[1] - t[0]
print(answer)