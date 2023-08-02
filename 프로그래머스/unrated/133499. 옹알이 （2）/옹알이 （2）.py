def solution(babbling):
    answer = 0
    
    for words in babbling:
        used = ''
        current_idx = 0
        while current_idx < len(words):
            if words[current_idx : current_idx+3] == 'aya':
                if used != 'aya':
                    used = 'aya'
                    current_idx += 3
                else:
                    break
            elif words[current_idx : current_idx+2] == 'ye':
                if used != 'ye':
                    used = 'ye'
                    current_idx += 2
                else:
                    break
            elif words[current_idx : current_idx+3] == 'woo':
                if used != 'woo':
                    used = 'woo'
                    current_idx += 3
                else:
                    break
            elif words[current_idx : current_idx+2] == 'ma':
                if used != 'ma':
                    used = 'ma'
                    current_idx += 2
                else:
                    break
            else:
                break
        if current_idx == len(words):
            answer += 1
            
    return answer