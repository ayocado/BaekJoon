def solution(cards1, cards2, goal):
    answer = 'Yes'
    cards1.append('')
    cards2.append('')
    idx1, idx2, idx_goal = 0, 0, 0
    
    while True:
        if idx_goal == len(goal):
            break
        if goal[idx_goal] == cards1[idx1]:
            idx_goal += 1
            idx1 += 1
        elif goal[idx_goal] == cards2[idx2]:
            idx_goal += 1
            idx2 += 1
        else:
            answer = 'No'
            break
            
    return answer