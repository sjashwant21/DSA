class Solution(object):
    def minimumOneBitOperations(self, n):
        count = 0
        while n>0:
            count ^= n
            n >>= 1
        return count