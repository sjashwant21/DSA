class Solution:
    def numSubmat(self, mat):
        m, n = len(mat), len(mat[0])
        heights = [0] * n
        total = 0

        for i in range(m):
            for j in range(n):
                heights[j] = heights[j] + 1 if mat[i][j] == 1 else 0

            for j in range(n):
                if heights[j] > 0:
                    min_height = heights[j]
                    k = j
                    while k >= 0 and heights[k] > 0:
                        min_height = min(min_height, heights[k])
                        total += min_height
                        k -= 1

        return total