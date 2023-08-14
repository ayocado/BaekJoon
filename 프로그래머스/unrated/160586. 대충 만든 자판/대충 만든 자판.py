def solution(keymap, targets):
    answer = []
    
    for target in targets:
        click_target = 0
        for alphabet in target:
            click_alpha = float('inf')
            for key in keymap:
                if alphabet not in key:
                    continue
                else:
                    click = key.index(alphabet) + 1
                    if click < click_alpha:
                        click_alpha = click
            if click_alpha == float('inf'):
                answer.append(-1)
                break
            click_target += click_alpha
        if click_alpha != float('inf'):
            answer.append(click_target)
    
    return answer