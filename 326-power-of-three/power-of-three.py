class Solution:
    def isPowerOfThree(self, n):
        # Loop approach
        if n <= 0:
            return False
        temp = n
        while temp % 3 == 0:
            temp //= 3
        if temp == 1:
            return True

        # Math-only fallback (largest 32-bit power of 3 is 3^19 = 1162261467)
        return 1162261467 % n == 0
