def solution(s):
    answer = 0
    x_cnt, notx_cnt = 0, 0
    x = ''
    
    for idx, word in enumerate(s):
        if x == '':
            x = word
        if word == x:
            x_cnt += 1
        else:
            notx_cnt += 1
        if x_cnt == notx_cnt:
            print(word)
            x = ''
            answer += 1
            x_cnt = 0
            notx_cnt = 0
        if idx == len(s) - 1 and x_cnt != notx_cnt:
            answer += 1
            
    return answer