class Solution:
    def maxFrequency(self, nums, k):
        # Sort the array in ascending order
        nums.sort()

        length = len(nums)

        # Calculate the differences between adjacent elements
        differences = [0] * length
        for i in range(1, length):
            differences[i] = nums[i] - nums[i - 1]

        # Calculate the prefix sums of the differences
        prefix_sums = [0] * length
        for i in range(1, length):
            prefix_sums[i] = prefix_sums[i - 1] + differences[i]

        low, high = 1, length

        # Binary search for the maximum frequency
        while low < high:
            mid = (high - low + 1) // 2 + low

            # Check if it's possible to achieve the given frequency with the allowed difference
            if self.isPossible(nums, differences, prefix_sums, mid, k):
                low = mid
            else:
                high = mid - 1

        return low

    def isPossible(self, nums, differences, prefix_sums, freq, k):
        length = len(differences)

        times = 0

        # Calculate the initial times based on the frequency and the last element in the subarray
        for i in range(freq - 2, -1, -1):
            times += nums[freq - 1] - nums[i]

        min_times = times

        # Iterate from freq-th element to the end of the array
        for i in range(freq, length):
            # Update times by considering the difference in prefix sums and new differences
            times = times - (prefix_sums[i - 1] - prefix_sums[i - freq]) + differences[i] * (freq - 1)
            min_times = min(min_times, times)

        # Check if the minimum times is within the allowed difference (k)
        return min_times <= k