from collections import deque

def solution(m, n, puddles):

    answer = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    answer[1][1] = 1
    
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            if i == 1 and j == 1:
                continue
            for puddle in puddles:
                if j == puddle[0] and i == puddle[1]:
                    break
            else:
                answer[i][j] = (answer[i - 1][j] + answer[i][j - 1]) % 1000000007
    
    return answer[n][m]
