class Solution(object):
    def maxTotalFruits(self, fruits, startPos, k):
        n = len(fruits)
        max_sum = 0
        total = 0
        left = 0
        for right in range(n):
            pos_r, amt_r = fruits[right]
            total += amt_r
            while left <= right:
                pos_l , _ = fruits[left]
                minSteps = min(
                    abs(startPos - pos_l) + (pos_r - pos_l),
                    abs(startPos - pos_r) + (pos_r - pos_l)
                )
                if minSteps <= k:
                    break
                total -= fruits[left][1]
                left += 1
            max_sum = max(max_sum,total)
        return max_sum
        