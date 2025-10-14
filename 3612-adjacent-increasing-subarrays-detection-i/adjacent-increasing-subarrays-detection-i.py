class Solution(object):
    def hasIncreasingSubarrays(self, nums, k):
        ranges = []
        start = 0
        n = len(nums)

        if k == 1:
            return True

        for i in range(1, n):
            if nums[i] <= nums[i - 1]: 
                ranges.append([start, i])
                start = i
        ranges.append([start, n])
        
        for i in range(len(ranges)):
            if ranges[i][1] - ranges[i][0] >= 2 * k:
                return True

            if i + 1 < len(ranges) and ranges[i][1] - ranges[i][0] >= k and ranges[i + 1][1] - ranges[i + 1][0] >= k:
                return True

        return False