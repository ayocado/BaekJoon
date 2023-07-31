def solution(dartResult):
    answer = 0
    cnt = 0
    first, second = '', ''
    
    for idx, string in enumerate(dartResult):
        if string in "SDT":
            cnt += 1
            if cnt == 3:
                third = dartResult[len(first)+len(second):]
            else:
                if dartResult[idx + 1] in "*#":
                    if cnt == 1:
                        first = dartResult[:idx+2]
                    elif cnt == 2:
                        second = dartResult[len(first):idx+2]
                else:
                    if cnt == 1:
                        first = dartResult[:idx+1]
                    elif cnt == 2:
                        second = dartResult[len(first):idx+1]
    
    if first[-1] == '*':
        if second[-1] == '*':
            if first[-2] == 'S':
                answer += int(first[:-2])**1 * 2 * 2
            elif first[-2] == 'D':
                answer += int(first[:-2])**2 * 2 * 2
            else:
                answer += int(first[:-2])**3 * 2 * 2
        else:
            if first[-2] == 'S':
                answer += int(first[:-2])**1 * 2
            elif first[-2] == 'D':
                answer += int(first[:-2])**2 * 2
            else:
                answer += int(first[:-2])**3 * 2
    elif first[-1] == '#':
        if second[-1] == '*':
            if first[-2] == 'S':
                answer += int(first[:-2])**1 * (-1) * 2
            elif first[-2] == 'D':
                answer += int(first[:-2])**2 * (-1) * 2
            else:
                answer += int(first[:-2])**3 * (-1) * 2
        else:
            if first[-2] == 'S':
                answer += int(first[:-2])**1 * (-1)
            elif first[-2] == 'D':
                answer += int(first[:-2])**2 * (-1)
            else:
                answer += int(first[:-2])**3 * (-1)
    else:
        if second[-1] == '*':
            if first[-1] == 'S':
                answer += int(first[:-1])**1 * 2
            elif first[-1] == 'D':
                answer += int(first[:-1])**2 * 2
            else:
                answer += int(first[:-1])**3 * 2
        else:
            if first[-1] == 'S':
                answer += int(first[:-1])**1
            elif first[-1] == 'D':
                answer += int(first[:-1])**2
            else:
                answer += int(first[:-1])**3
    
    if second[-1] == '*':
        if third[-1] == '*':
            if second[-2] == 'S':
                answer += int(second[:-2])**1 * 2 * 2
            elif second[-2] == 'D':
                answer += int(second[:-2])**2 * 2 * 2
            else:
                answer += int(second[:-2])**3 * 2 * 2
        else:
            if second[-2] == 'S':
                answer += int(second[:-2])**1 * 2
            elif second[-2] == 'D':
                answer += int(second[:-2])**2 * 2
            else:
                answer += int(second[:-2])**3 * 2
    elif second[-1] == '#':
        if third[-1] == '*':
            if second[-2] == 'S':
                answer += int(second[:-2])**1 * (-1) * 2
            elif second[-2] == 'D':
                answer += int(second[:-2])**2 * (-1) * 2
            else:
                answer += int(second[:-2])**3 * (-1) * 2
        else:
            if second[-2] == 'S':
                answer += int(second[:-2])**1 * (-1)
            elif second[-2] == 'D':
                answer += int(second[:-2])**2 * (-1)
            else:
                answer += int(second[:-2])**3 * (-1)
    else:
        if third[-1] == '*':
            if second[-1] == 'S':
                answer += int(second[:-1])**1 * 2
            elif second[-1] == 'D':
                answer += int(second[:-1])**2 * 2
            else:
                answer += int(second[:-1])**3 * 2
        else:
            if second[-1] == 'S':
                answer += int(second[:-1])**1
            elif second[-1] == 'D':
                answer += int(second[:-1])**2
            else:
                answer += int(second[:-1])**3
    
    if third[-1] == '*':
        if third[-2] == 'S':
            answer += int(third[:-2])**1 * 2
        elif third[-2] == 'D':
            answer += int(third[:-2])**2 * 2
        else:
            answer += int(third[:-2])**3 * 2
    elif third[-1] == '#':
        if third[-2] == 'S':
            answer += int(third[:-2])**1 * (-1)
        elif third[-2] == 'D':
            answer += int(third[:-2])**2 * (-1)
        else:
            answer += int(third[:-2])**3 * (-1)
    else:
        if third[-1] == 'S':
            answer += int(third[:-1])**1
        elif third[-1] == 'D':
            answer += int(third[:-1])**2
        else:
            answer += int(third[:-1])**3
            
    return answer