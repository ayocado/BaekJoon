def solution(numbers):
    answer = []
    numbers.sort()
    
    for idx, number1 in enumerate(numbers):
        for number2 in numbers[idx + 1:]:
            if number1 + number2 not in answer:
                answer.append(number1 + number2)
                
    return sorted(answer)