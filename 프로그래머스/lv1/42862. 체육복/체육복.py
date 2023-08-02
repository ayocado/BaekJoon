def solution(n, lost, reserve):

    for student in range(1, n+1):
        if student in lost and student in reserve:
            lost.remove(student)
            reserve.remove(student)

    answer = n - len(lost)
    borrowed = []
    lost.sort()
    reserve.sort()
    
    for lost_student in lost:
        if lost_student - 1 in reserve and lost_student - 1 not in borrowed:
            answer += 1
            borrowed.append(lost_student - 1)
        elif lost_student + 1 in reserve and lost_student + 1 not in borrowed:
            answer += 1
            borrowed.append(lost_student + 1)
        else:
            continue
            
    return answer