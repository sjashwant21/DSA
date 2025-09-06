class Solution(object):
    def minOperations(self, queries):
        a=0
        for q in queries:
            l,r=q 
            t=0 
            ln=1 
            ln2=1
            while ln<=r:
                s=max(l,ln)
                e=min(r,ln*4-1)
                if e>=s:
                    t+= (e-s+1)*ln2
                ln*= 4
                ln2+=1
            a+=(t//2)+(t%2) #total number of steps in this query ceil without ceil
        return a