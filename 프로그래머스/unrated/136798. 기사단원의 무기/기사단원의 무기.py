def divisor(num):
    divisor_set = set()
    for i in range(1, int(num ** 0.5) + 1):
        if num % i == 0:
            divisor_set.add(i)
            divisor_set.add(num // i)
    return len(divisor_set)


def solution(number, limit, power):
    answer = 0
    
    for num in range(1, number + 1):
        if divisor(num) <= limit:
            answer += divisor(num)
        else:
            answer += power
            
    return answer