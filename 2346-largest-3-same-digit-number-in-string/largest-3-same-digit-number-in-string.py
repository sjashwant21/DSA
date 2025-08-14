class Solution:
    def largestGoodInteger(self, num):
        best = ""
        for i in range(len(num) - 2):
            sub = num[i:i+3]
            if sub[0] == sub[1] == sub[2]:
                if sub > best:
                    best = sub
        return best
