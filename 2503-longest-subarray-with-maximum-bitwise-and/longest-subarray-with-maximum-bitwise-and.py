class Solution:
    def longestSubarray(self,nums):
        max_num = max(nums)
        max_len = 0
        cur_len = 0

        for num in nums:
            if num == max_num:
                cur_len += 1
                max_len = max(max_len, cur_len)
            else:
                cur_len = 0

        return max_len