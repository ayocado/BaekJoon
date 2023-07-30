def solution(n):
    numlist = [True] * (n+1)
    numlist[0] = False
    numlist[1] = False
    
    for num in range(2, int(n ** 0.5) + 1):
        i = 2
        while num * i <= n:
            numlist[num * i] = False
            i += 1
    
    return numlist.count(True)