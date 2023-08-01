def solution(lottos, win_nums):
    zero = 0
    correct = 0
    rank = {0:6, 1:6, 2:5, 3:4, 4:3, 5:2, 6:1}
    
    for lotto_num in lottos:
        if lotto_num == 0:
            zero += 1
        elif lotto_num in win_nums:
            correct += 1
            
    return [rank[correct + zero], rank[correct]]