class Solution(object):
    def avoidFlood(self, rains):
        r=[-1]*len(rains)
        full={}
        z_days=[]
        for i,lake in enumerate(rains):
            if lake==0:
                z_days.append(i)
            else:
                if lake in full:
                    l,ridx=0,0
                    while ridx<len(z_days) and z_days[ridx]<=full[lake]:
                        ridx+=1
                    if ridx==len(z_days):
                        return []
                    r[z_days[ridx]]=lake
                    z_days.pop(ridx)
                full[lake]=i
        for d in z_days:
            r[d]=1
        return r