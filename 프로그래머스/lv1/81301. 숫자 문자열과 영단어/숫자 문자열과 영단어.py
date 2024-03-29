def solution(s):
    answer = ''
    dictionary = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    
    word = ''
    for i in s:
        if i in '0123456789':
            answer += i
        else:
            word += i
            if word in list(dictionary.keys()):
                answer += dictionary[word]
                word = ''
                
    return int(answer)