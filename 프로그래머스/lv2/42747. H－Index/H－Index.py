# 문제링크 : https://school.programmers.co.kr/learn/courses/30/lessons/42747

def solution(citations):
    citations.sort(reverse=True)
    answer = []
    
    for citation in range(max(citations) + 1):
        higher = []
        for check in citations:
            if check >= citation:
                higher.append(check)
        
        if len(higher) >= citation and len(citations) - len(higher) <= citation:
            answer.append(citation)
    
    return max(answer)