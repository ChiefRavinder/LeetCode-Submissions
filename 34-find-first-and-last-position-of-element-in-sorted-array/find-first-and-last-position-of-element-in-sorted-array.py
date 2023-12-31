class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target not in nums:
            return [-1,-1]
        
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if nums[mid]==target:
                start=mid
                end=mid
                while start>0 and nums[start-1]==target:
                    start-=1
                while end<len(nums)-1 and nums[end+1]==target:
                    end+=1
                return [start,end]
            elif nums[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return [-1,-1]

