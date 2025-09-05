class Solution(object):
    def makeTheIntegerZero(self, num1, num2):
        for op in range(1, 61):
            rem = num1 - op * num2
            if rem < op:
                continue
            if bin(rem).count("1") <= op <= rem:
                return op
        return -1