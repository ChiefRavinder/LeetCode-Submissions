class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is a positive integer and a power of 4
        return n > 0 and (n & (n - 1)) == 0 and n % 3 == 1
