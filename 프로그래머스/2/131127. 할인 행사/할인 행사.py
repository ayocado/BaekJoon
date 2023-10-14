from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    for idx in range(len(discount) - 9):
        d_lst = dict(Counter(discount[idx : idx + 10]))
        cnt = 0
        
        try:
            for i in range(len(want)):
                if d_lst[want[i]] == number[i]:
                    cnt += 1
            if cnt == len(want):
                answer += 1
        except:
            continue
    
    return answer