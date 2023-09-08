class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        result=[]
        for i in range (1,numRows+1):
            temp=[]
            for j in range (i):
                if j==0 or j==i-1:
                    temp.append(1)
                else:
                    k=result[i-2][j-1]+result[i-2][j]
                    temp.append(k)
            result.append(temp)
        return result