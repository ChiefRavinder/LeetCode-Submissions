class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        m=(bin(n)[2:])
        p=str(m)
        count=0
        print(m)
        for ch in p:
            if ch=='1':
                count+=1

        return count