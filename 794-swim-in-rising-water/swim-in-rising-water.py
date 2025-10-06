import heapq

class Solution(object):
    def swimInWater(self, grid):
        n = len(grid) 
        heap = [(grid[0][0], 0, 0)] 
        d = [(1,0), (-1,0), (0,1), (0,-1)]  
        s = set()  
        mh = 0  
        
        while heap:
            h, r, c = heapq.heappop(heap)  
            mh = max(mh, h) 
            
            if r == (n-1) and c == (n-1):  
                return mh
            
            if (r, c) in s:
                continue
            s.add((r, c))  
            
            for i, j in d: 
                nr, nc = r + i, c + j 
                if 0 <= nr < n and 0 <= nc < n and (nr, nc) not in s:
                    heapq.heappush(heap, (grid[nr][nc], nr, nc))