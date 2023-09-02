class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices:
            return 0
        
        low=0
        high=1
        maxProfit=0

        while (high<len(prices)):
            if prices[low]<prices[high]:
                profit=prices[high]-prices[low]
                maxProfit=max(maxProfit,profit)
            else:
                low=high
            high+=1
        return maxProfit
