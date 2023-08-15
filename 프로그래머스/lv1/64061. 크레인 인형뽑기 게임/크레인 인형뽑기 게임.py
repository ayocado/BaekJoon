def solution(board, moves):
    answer = 0
    bucket = []
    
    for move in moves:
        for idx, row in enumerate(board):
            if row[move - 1] == 0:
                continue
            else:
                bucket.append(row[move - 1])
                row[move - 1] = 0
                break
        if len(bucket) >= 2:
            if bucket[-2] == bucket[-1]:
                bucket.pop()
                bucket.pop()
                answer += 2
                
    return answer