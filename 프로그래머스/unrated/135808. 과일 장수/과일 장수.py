def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    box = len(score) // m
    
    for box_num in range(box):
        fruit = score[box_num * m : (box_num + 1) * m]
        answer += min(fruit) * m
        
    return answer