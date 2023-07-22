def solution(food):
    answer = ''
    
    for idx, cnt in enumerate(food):
        if idx == 0:
            continue
        else:
            answer += str(idx) * (cnt // 2)
    
    answer_reverse = ''.join(list(reversed(answer)))
    
    return answer + '0' + answer_reverse