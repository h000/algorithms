class Solution(object):
    def uniquePaths(self, m, n):
        answer = [[0 for _ in range(n)] for _ in range(m)]
        for i in range(m):
            answer[i][0] = 1
        for j in range(n):
            answer[0][j] = 1

        for i in range(1, m):
            for j in range(1, n):
                answer[i][j] = answer[i - 1][j] + answer[i][j - 1]
        return answer[m - 1][n - 1]
