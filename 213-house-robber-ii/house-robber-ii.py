class Solution:
    def rob(self, nums: List[int]) -> int:
        def f(n, dp, arr):
            if n == 0:
                return arr[0]
            if dp[n] != -1:
                return dp[n]
            if n < 0:
                return 0
            pick = arr[n] + f(n - 2, dp, arr)
            nopick = 0 + f(n - 1, dp, arr)
            dp[n] = max(pick, nopick)
            return dp[n]

        n = len(nums)
        if n == 1:
            return nums[0]
        dp1 = [-1] * (n - 1)
        dp2 = [-1] * (n - 1)
        first = f(n - 2, dp1, nums[1:])
        second = f(n - 2, dp2, nums[:-1])
        return max(first, second)
