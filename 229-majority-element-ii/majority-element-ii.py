import math
class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        out=set()
        for i in nums:
            if nums.count(i)>math.ceil(len(nums)//3):
                out.add(i)
        return out
        