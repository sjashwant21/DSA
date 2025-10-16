class Solution(object):
    def findSmallestInteger(self, nums, value):
        h = {} 
        for i in nums:  
            r = i % value
            if r < 0:  
                r += value
            if r in h:  
                h[r] += 1
            else:
                h[r] = 1
        
        i = 0 
        while h.get(i % value) > 0: 
            h[i % value] -= 1  
            i += 1 
        return i  