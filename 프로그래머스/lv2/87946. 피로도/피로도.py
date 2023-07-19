from itertools import permutations

def solution(k, dungeons):
    answer = 0
    dungeons_n = len(dungeons)
    dungeons_list = list(permutations(dungeons, dungeons_n))
    
    for dungeons_point in dungeons_list:
        k_point = k
        count = 0
        for dungeon in dungeons_point:
            if k_point >= dungeon[0]:
                k_point -= dungeon[1]
                count += 1
            else:
                break
        if answer < count:
            answer = count
    
    return answer