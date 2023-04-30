class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        money = [nums[0],max(nums[0], nums[1])]
        for i in range(2, len(nums)):
            money.append(max(money[i - 1], money[i - 2] + nums[i]))
        return money[len(nums) - 1]
