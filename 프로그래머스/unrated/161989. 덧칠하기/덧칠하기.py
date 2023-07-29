def solution(n, m, section):
    answer = 1
    current_wall = section[0] + m
    
    for wall in section:
        if current_wall == wall:
            current_wall += m
            answer += 1
        elif current_wall < wall:
            current_wall = wall + m
            answer += 1
        else:
            continue
            
    return answer