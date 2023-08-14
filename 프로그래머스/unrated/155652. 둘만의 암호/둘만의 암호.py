def solution(s, skip, index):
    answer = ''
    notskip = ''
    alphabets = 'abcdefghijklmnopqrstuvwxyz'
    for alphabet in alphabets:
        if alphabet not in skip:
            notskip += alphabet
    
    for s_word in s:
        idx = (notskip.index(s_word) + index) % len(notskip)
        answer += notskip[idx]
        
    return answer