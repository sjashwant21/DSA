class Solution(object):
    def mergeArrays(self, nums1, nums2):
        d = {}
        for i, v in nums1:
            d[i] = d.get(i, 0) + v
        for i, v in nums2:
            d[i] = d.get(i, 0) + v
        return sorted(d.items())