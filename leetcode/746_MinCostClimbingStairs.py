class Solution(object):
    def minCostClimbingStairs(self, cost):
        total = [0, 0]
        for i in range(2, len(cost) + 1):
            total.append(min(total[i - 1] + cost[i - 1], total[i - 2] + cost[i - 2]))
        return total[len(cost)]
