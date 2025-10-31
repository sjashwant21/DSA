class Solution(object):
    def getSneakyNumbers(self, nums):
        seen = set()
        r = []
        for i in nums:
            if i in seen:
                r.append(i)
            else:
                seen.add(i)
        return r