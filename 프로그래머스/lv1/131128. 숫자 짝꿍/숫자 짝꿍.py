def solution(X, Y):
    answer = ''
    x_set = list(set(X))
    y_set = list(set(Y))
    
    if len(x_set) >= len(y_set):
        maxlist = x_set
    else:
        maxlist = y_set
    
    maxlist.sort(reverse=True)
    
    for num in maxlist:
        num_cnt = min(X.count(num), Y.count(num))
        answer += num * num_cnt
    
    if answer == '':
        return str(-1)
    elif set(answer) == {'0'}:
        return str(0)
    else:
        return answer