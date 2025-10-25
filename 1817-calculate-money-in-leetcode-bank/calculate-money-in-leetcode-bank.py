class Solution(object):
    def totalMoney(self, n):
        return self.amount(n)
    def amount(self, day):
        i = 0
        j = 0
        l = []
        for k in range(day):
            if k % 7 == 0:
                i += 1
                j = i
                l.append(j)
            else:
                j += 1
                l.append(j)
        return sum(l)