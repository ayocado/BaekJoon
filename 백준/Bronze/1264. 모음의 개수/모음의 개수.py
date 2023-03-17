import sys

sentence = ''
answer = []
while True:
    noun = 0
    sentence = sys.stdin.readline().rstrip()
    if sentence == '#':
        break
    else:
        noun += sentence.count('a')
        noun += sentence.count('e')
        noun += sentence.count('i')
        noun += sentence.count('o')
        noun += sentence.count('u')
        noun += sentence.count('A')
        noun += sentence.count('E')
        noun += sentence.count('I')
        noun += sentence.count('O')
        noun += sentence.count('U')
        answer.append(noun)

for i in range(len(answer)):
    if i == len(answer) - 1:
        print(answer[i], end='')
    else:
        print(answer[i])