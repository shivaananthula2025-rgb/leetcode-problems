class Solution(object):
    def rob(self, nums):
        dp = [-1] * len(nums)
        return self.calculate(nums, len(nums) - 1, dp)

    def calculate(self, nums, n, dp):
        if n < 0:
            return 0

        if n == 0:
            return nums[0]

        if dp[n] != -1:
            return dp[n]

        dp[n] = max(
            self.calculate(nums, n - 1, dp),
            nums[n] + self.calculate(nums, n - 2, dp)
        )

        return dp[n]