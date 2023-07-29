def solution(N, stages):
    stages.sort()
    stages_set = list(set(stages))
    failure_dict = {}
    
    for n in range(1, N+1):
        if n in stages_set:
            n_idx = stages.index(n)
            n_cnt = stages.count(n)
            failure = len(stages[n_idx : n_idx + n_cnt]) / len(stages[n_idx:])
            failure_dict[n] = failure
        else:
            failure_dict[n] = 0
    
    return sorted(failure_dict, key = lambda x: failure_dict[x], reverse=True)
            