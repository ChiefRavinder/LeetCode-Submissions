class Solution:
    def minOperations(self, nums):
        n = len(nums)
        nums.sort()  # Sort the input nums in non-decreasing order.
        
        if n == 1:
            return 0  # If there's only one element, no operations are needed.
        
        mini = float('inf')  # Initialize the minimum operations to a very large value.
        v = [0] * (n + 1)  # Create a list to store prefix sums.
        mp = {}  # Create a dictionary to store the frequency of each element.

        count = 0  # Initialize a count variable.
        
        # Calculate prefix sums and update the count of repeated elements.
        for i in range(n):
            mp[nums[i]] = mp.get(nums[i], 0) + 1
            if mp[nums[i]] != 1:
                count += 1
            v[i] = count
        v[n] = v[n - 1]  # Set the last element of v to be the same as the second-to-last.

        for i in range(n - 1):
            idx = self.lower_bound(nums, nums[i] + n - 1)  # Find the index of the upper bound.
            x = i

            if idx != n and nums[idx] != nums[i] + n - 1:
                x += 1
            if idx == n:
                x += 1

            x += n - 1 - idx
            x += v[idx] - v[i]  # Calculate the number of operations required.
            mini = min(mini, x)  # Update the minimum operations.

        return mini  # Return the minimum operations required.

    def lower_bound(self, nums, target):
        left, right = 0, len(nums)
        while left < right:
            mid = left + (right - left) // 2
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid
        return left  # Return the index of the lower bound.