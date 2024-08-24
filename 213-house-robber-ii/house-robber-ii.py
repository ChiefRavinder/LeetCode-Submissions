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
            nopick = f(n - 1, dp, arr)
            dp[n] = max(pick, nopick)
            return dp[n]

        n = len(nums)
        if n == 1:
            return nums[0]

        # Handle two cases: 
        # 1. Exclude the first house and include the last house
        # 2. Include the first house and exclude the last house

        dp1 = [-1] * (n - 1)  # DP array for the case where we exclude the last house
        dp2 = [-1] * (n - 1)  # DP array for the case where we exclude the first house
        
        first = f(n - 2, dp1, nums[1:])  # Exclude the first house (nums[1:] part)
        second = f(n - 2, dp2, nums[:-1])  # Exclude the last house (nums[:-1] part)
        
        return max(first, second)
