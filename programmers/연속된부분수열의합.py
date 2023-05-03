def solution(sequence, k):
    acc = []
    n = 0
    for s in sequence:
        n += s
        acc.append(n)
    i = 0
    j = 0
    answer = []
    while i < len(acc) and j < len(acc):
        sm = acc[j] - acc[i] + sequence[i]
        if sm == k:
            if not answer or answer[1] - answer[0] > j - i:
                answer = [i, j]
            i += 1
            j += 1
        elif sm < k:
            j += 1
        else:
            i += 1
    
    return answer
