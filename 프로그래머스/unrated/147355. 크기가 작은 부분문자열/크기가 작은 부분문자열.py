def solution(t, p):
    answer = 0
    
    for i in range(len(p), len(t)+1):
        if int(t[i-len(p): i]) <= int(p):
            answer += 1
            
    return answer