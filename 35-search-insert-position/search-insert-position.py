class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low=0
        high=len(nums)-1
        found=False 
        while (low<=high and not found):
            mid=(low+high)//2
            if target==nums[mid]:
                found=True
                return mid
            elif target > nums[mid] :
                low=mid+1
            else:
                high=mid-1
        return low
        