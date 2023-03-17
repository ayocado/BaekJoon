import sys

club = []
while True:
    name, age, weight = map(str, sys.stdin.readline().split())
    if name == '#' and age == '0' and weight == '0':
        break
    else:
        if int(age) > 17 or int(weight) >= 80:
            club.append(f'{name} Senior')
        else:
            club.append(f'{name} Junior')

for i in range(len(club)):
    if i == len(club) - 1:
        print(club[i], end='')
    else:
        print(club[i])