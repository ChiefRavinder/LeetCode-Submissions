class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        # Find leftmost occurrence
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                start = mid
                end = mid

                # Find the start of the range
                while start > 0 and nums[start - 1] == target:
                    start -= 1

                # Find the end of the range
                while end < len(nums) - 1 and nums[end + 1] == target:
                    end += 1

                return [start, end]

            elif target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return [-1, -1]