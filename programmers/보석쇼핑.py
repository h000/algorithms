def solution(gems):
    answer = []
    
    d = dict()
    total = len(set(gems))
    current = 1
    start = -1
    end = -1
    
    s = 0
    e = 0
    d[gems[s]] = 1
    while s <= e and e < len(gems):
        if d.get(gems[s], 0) > 1:
            d[gems[s]] = d.get(gems[s], 0) - 1
            s += 1
        elif current < total:
            e += 1
            if e < len(gems):
                d[gems[e]] = d.get(gems[e], 0) + 1
                current += 1 if d.get(gems[e]) == 1 else 0
        else:
            if (start < 0 and end < 0) or (e - s < end - start):
                start = s
                end = e
            
            s += 1
            e = s
            if e < len(gems):
                current = 1
                d = dict()
                d[gems[s]] = 1
    
    return [start + 1, end + 1]
