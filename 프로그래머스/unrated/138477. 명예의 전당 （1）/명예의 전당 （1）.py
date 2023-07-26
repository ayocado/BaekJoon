def solution(k, score):
    answer, board = [], []
    for s in score:
        board.append(s)
        board.sort(reverse=True)
        if len(board) > k:
            board.pop()
        answer.append(board[-1])
    return answer