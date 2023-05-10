def solution(n, s):
    if s < n:
        return [-1]
    answer = []
    
    x = s // n
    y = s % n
    for i in range(n):
        if i >= n - y:
            answer.append(x + 1)
        else:
            answer.append(x)
    return answer
