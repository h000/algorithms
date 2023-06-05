def solution(scores):
    wanho = scores[0]
    
    scores.sort(key=lambda x : (-x[0], -x[1]))
    total = []
    
    i = 0
    sm = 0
    while i < len(scores):
        j = i
        while j < len(scores) and scores[j][0] == scores[i][0]:
            if scores[j][1] >= sm:
                total.append(scores[j][0] + scores[j][1])
            elif wanho[0] == scores[j][0] and wanho[1] == scores[j][1]:
                return -1
            j += 1
        sm = max(sm,scores[i][1])
        i = j
    
    total.sort(key=lambda x : -x)
    
    return total.index(wanho[0] + wanho[1]) + 1
