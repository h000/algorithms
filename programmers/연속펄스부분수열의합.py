def solution(sequence):  
    total = [sequence[0]]
    flag = -1
    for s in sequence[1:]:
        total.append(total[-1] + flag * s)
        flag *= -1
    
    
    return max(max(total), abs(min(total)), max(total) - min(total))
