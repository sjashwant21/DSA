from collections import Counter
class Solution(object):
    def maxFrequencyElements(self, nums):
        freq = Counter(nums)
        maxFreq = max(freq.values())
        return sum(v for v in freq.values() if v == maxFreq)