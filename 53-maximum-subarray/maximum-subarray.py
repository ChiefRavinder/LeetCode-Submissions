class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSum=nums[0]
        currSum=nums[0]

        for i in nums[1::]:
            currSum=max(i,currSum+i)
            maxSum=max(maxSum,currSum)

        return maxSum
        
        
        

