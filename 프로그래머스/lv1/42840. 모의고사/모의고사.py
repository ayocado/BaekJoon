def solution(answers):
    one = [1,2,3,4,5]
    two = [2,1,2,3,2,4,2,5]
    three = [3,3,1,1,2,2,4,4,5,5]
    score_1, score_2, score_3 = 0, 0, 0
    result = []
    
    for idx, answer in enumerate(answers):
        if one[idx % 5] == answer:
            score_1 += 1
        if two[idx % 8] == answer:
            score_2 += 1
        if three[idx % 10] == answer:
            score_3 += 1
            
    highest = max(score_1, score_2, score_3)
    if score_1 == highest:
        result.append(1)
    if score_2 == highest:
        result.append(2)
    if score_3 == highest:
        result.append(3)
    
    return result