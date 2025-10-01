class Solution:
    def numWaterBottles(self, b, n):
        return b + (b - 1) // (n - 1)