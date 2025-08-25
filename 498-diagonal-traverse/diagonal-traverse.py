class Solution:
    def findDiagonalOrder(self, mat):
        if not mat or not mat[0]:
            return []

        m, n = len(mat), len(mat[0])
        result = []
        row, col = 0, 0
        direction = 1  # 1 = up-right, -1 = down-left

        for _ in range(m * n):
            result.append(mat[row][col])

            if direction == 1:  # moving up-right
                if col == n - 1:      # last column → go down
                    row += 1
                    direction = -1
                elif row == 0:        # first row → go right
                    col += 1
                    direction = -1
                else:                 # move up-right
                    row -= 1
                    col += 1
            else:  # moving down-left
                if row == m - 1:      # last row → go right
                    col += 1
                    direction = 1
                elif col == 0:        # first column → go down
                    row += 1
                    direction = 1
                else:                 # move down-left
                    row += 1
                    col -= 1

        return result
