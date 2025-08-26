import math

class Solution:
    def areaOfMaxDiagonal(self, dimensions):
        max_diag = -1
        max_area = -1

        for length, width in dimensions:
            diag = math.sqrt(length * length + width * width)
            area = length * width

            # First priority: longest diagonal
            if diag > max_diag:
                max_diag = diag
                max_area = area
            # Second priority: larger area if diagonals are equal
            elif abs(diag - max_diag) < 1e-9 and area > max_area:
                max_area = area

        return max_area
