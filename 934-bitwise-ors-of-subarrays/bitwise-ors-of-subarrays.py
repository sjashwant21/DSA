class Solution:
    def subarrayBitwiseORs(self, arr):
        res = set()
        curr = set()
        for num in arr:
            curr = {num | x for x in curr} | {num}
            res |= curr
        return len(res)