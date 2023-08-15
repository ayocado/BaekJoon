def distance(start, goal):
    if start == '*':
        start = 10
    elif start == 0:
        start = 11
    elif start == '#':
        start = 12
    
    if goal == 0:
        goal = 11
        
    if start < goal:
        return (goal - start) % 3 + (goal - start) // 3
    else:
        return (start - goal) % 3 + (start - goal) // 3
    
def solution(numbers, hand):
    answer = ''
    left, right = '*', '#'
    
    for number in numbers:
        if number in [1, 4, 7]:
            answer += 'L'
            left = number
        elif number in [3, 6, 9]:
            answer += 'R'
            right = number
        else:
            if distance(left, number) < distance(right, number):
                answer += 'L'
                left = number
            elif distance(left, number) > distance(right, number):
                answer += 'R'
                right = number
            else:
                if hand == 'left':
                    answer += 'L'
                    left = number
                else:
                    answer += 'R'
                    right = number
                    
    return answer