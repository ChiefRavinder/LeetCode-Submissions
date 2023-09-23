class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxnum=float('-inf')
        result=[]
        for i in candies:
            if i>maxnum:
                maxnum=i
        for i in candies:
            if (i + extraCandies >= maxnum):
                result.append(True)
            else:
                result.append(False)
        return result

