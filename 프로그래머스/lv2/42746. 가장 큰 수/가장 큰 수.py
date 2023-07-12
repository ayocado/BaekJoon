# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42746

from itertools import permutations
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: (x * 4)[:4], reverse=True)
    answer = ''.join(numbers)
    return str(int(answer))