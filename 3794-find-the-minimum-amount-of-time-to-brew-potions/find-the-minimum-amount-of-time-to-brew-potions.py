class Solution(object):
    def minTime(self, skill, mana):

        n=len(skill) 
        t=[0]*n 

        for x in mana: 
            t[0] += skill[0] *x 
            for i in range(1,n): 
                t[i] =max(t[i],t[i-1]) + skill[i]*x

            for i in range(n-2,-1,-1):
                t[i] = t[i+1] - skill[i+1]*x

        return t[-1] 