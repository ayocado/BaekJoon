def solution(name, yearning, photo):
    answer = []
    yearn_dict = dict(zip(name, yearning))
    
    for photo_part in photo:
        yearn_score = 0
        for photo_person in photo_part:
            if photo_person in name:
                yearn_score += yearn_dict[photo_person]
        answer.append(yearn_score)
        
    return answer