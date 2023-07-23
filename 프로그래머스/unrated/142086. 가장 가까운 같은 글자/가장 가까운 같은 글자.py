def solution(s):
    answer = []
    for idx, word in enumerate(s):
        if idx == 0:
            answer.append(-1)
        else:
            reverse_s = ''.join(reversed(s[:idx]))
            flag = 0
            for idx_check, word_check in enumerate(reverse_s):
                if word == word_check:
                    answer.append(idx_check + 1)
                    flag = 1
                    break
            if flag == 0:
                answer.append(-1)
                
    return answer