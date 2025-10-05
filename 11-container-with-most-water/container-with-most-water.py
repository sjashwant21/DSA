class Solution:
    def maxArea(self, height: list[int]) -> int:
        i, j = 0, len(height) - 1
        max_area = 0
        while i < j:
            max_area = max(max_area, (j - i) * min(height[i], height[j]))
            if height[j] > height[i]:
                i += 1
            else:
                j -= 1
        return max_area