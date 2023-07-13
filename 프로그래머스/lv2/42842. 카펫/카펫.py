def solution(brown, yellow):
    for i in range(3, int((brown + yellow + 1) ** (1/2)) + 1):
        if (brown + yellow) % i == 0:
            y = i
            x = (brown + yellow) // i
            
            if (2*x + 2*y - 4) == brown and (x - 2)*(y - 2) == yellow:
                return [x, y]