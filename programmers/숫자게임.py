def solution(A, B):
    answer = 0
    A.sort()
    B.sort()
    i = len(A) - 1
    j = len(B) - 1
    while i >= 0 and j >= 0:
        if A[i] < B[j]:
            answer += 1
            i -= 1
            j -= 1
        else:
            i -= 1
    return answer
