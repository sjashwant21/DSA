class Solution(object):
    def sumZero(self, n):
        return [ n * (1 - n) // 2] + list(range(1, n))