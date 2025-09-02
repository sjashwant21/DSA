from collections import defaultdict

class Solution(object):
    def numberOfPairs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        # Sort by x ascending, then y descending
        px = sorted(points, key=lambda p:(p[0], -p[1]))
        blocked = defaultdict(set)
        res = 0
        for p in range(len(px) - 2, -1, -1):
            for p2 in range(p + 1, len(px)):
                if p2 in blocked[p]:
                    continue
                xp, yp = px[p]
                xp2, yp2 = px[p2]
                if xp <= xp2 and yp >= yp2:
                    # Found a valid pair
                    res += 1
                    # Block all rectangles that were blocked for p2 as well
                    blocked[p].add(p2)
                    blocked[p].update(blocked[p2])
        return res