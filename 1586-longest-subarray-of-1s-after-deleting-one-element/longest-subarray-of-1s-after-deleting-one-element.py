class Solution:
    def longestSubarray(self, nums):
        left = 0
        zero_count = 0
        max_len = 0

        for right in range(len(nums)):
            if nums[right] == 0:
                zero_count += 1

            # shrink window if more than 1 zero
            while zero_count > 1:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1

            # window size - 1 (because we must delete one element)
            max_len = max(max_len, right - left)

        return max_len