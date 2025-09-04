class Solution(object):
    def findClosest(self, x, y, z):
        p1 = abs(z-x)
        p2 = abs(z-y)

        if p2 > p1:
            return 1
        if p1 > p2:
            return 2
        else:
            return 0