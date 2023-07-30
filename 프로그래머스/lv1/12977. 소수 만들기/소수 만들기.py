from itertools import combinations

def solution(nums):
    numlist = list(combinations(nums, 3))
    sumlist = list(map(lambda x: sum(x), numlist))
    sumlist_set = list(set(sumlist))
    answerlist = []
    answer = 0
    
    for number in sumlist_set:
        flag = 0
        for i in range(2,number):
            if number % i == 0:
                flag = 1
                break
        if flag == 0:
            answerlist.append(number)
    
    for number in answerlist:
        answer += sumlist.count(number)
        
    return answer