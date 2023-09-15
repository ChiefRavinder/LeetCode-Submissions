class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1, -1]

        # Find the leftmost occurrence of the target
        left = self.findLeft(nums, target)

        # Find the rightmost occurrence of the target
        right = self.findRight(nums, target)

        return [left, right]

    def findLeft(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low) // 2
            if nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        return low if nums[low] == target else -1

    def findRight(self, nums, target):
        low = 0
        high = len(nums) - 1
        while low < high:
            mid = low + (high - low + 1) // 2  # Ensure mid biases towards the right
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid
        return low if nums[low] == target else -1
