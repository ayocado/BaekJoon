from itertools import permutations

def solution(numbers):
    answer = []
    for i in range(1, len(numbers) + 1):
        made_numbers = list(permutations(numbers, i))
        for made_number in made_numbers:
            flag = 0
            made_number = int(''.join(made_number))
            if made_number == 0 or made_number == 1:
                pass
            else:
                for check in range(2, made_number):
                    if made_number % check == 0:
                        flag = 1
                        break
                if flag == 0 and made_number not in answer:
                    answer.append(made_number)
    return len(answer)