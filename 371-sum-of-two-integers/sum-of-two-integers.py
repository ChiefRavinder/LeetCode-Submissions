class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        mask = 0xFFFFFFFF
        while b:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)