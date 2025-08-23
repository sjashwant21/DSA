class Solution(object):
    def minimumSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        self.n = len(grid)
        self.m = len(grid[0])
        self.grid = grid
        return self.solve()

    def helper(self,u,d,l,r):
        min_i = self.n
        max_i = 0
        min_j = self.m
        max_j = 0
        for i in range(u,d+1):
            for j in range(l,r+1):
                if self.grid[i][j]==1:
                    min_i = min(min_i,i)
                    max_i = max(max_i,i)
                    min_j = min(min_j,j)
                    max_j = max(max_j,j)
        ans = ((max_i-min_i+1)*(max_j-min_j+1)) 
        # print(ans,u,d,l,r)
        return ans if min_i<=max_i else float("inf")


    def solve(self):
        res = self.n*self.m
        # Three rows
        for i in range(self.n-2):
            for j in range(i+1,self.n-1):
                res = min(res,
                self.helper(0,i,0,self.m-1)+
                self.helper(i+1,j,0,self.m-1)+
                self.helper(j+1,self.n-1,0,self.m-1)
                )
        # Three cols
        for i in range(self.m-2):
            for j in range(i+1,self.m-1):
                res = min(res,
                self.helper(0,self.n-1,0,i)+
                self.helper(0,self.n-1,i+1,j)+
                self.helper(0,self.n-1,j+1,self.m-1)
                )
        
        for i in range(self.n-1):
            for j in range(self.m-1):
                # Up strip, Bottom left, Bottom right
                res = min(res,
                self.helper(0,i,0,self.m-1)+
                self.helper(i+1,self.n-1,0,j)+
                self.helper(i+1,self.n-1,j+1,self.m-1)
                )
                # Up right, Up left, Bottom strip
                res = min(res,
                self.helper(0,i,0,j)+
                self.helper(0,i,j+1,self.m-1)+
                self.helper(i+1,self.n-1,0,self.m-1)
                )

                # Left strip, right up, right bottom
                res = min(res,
                self.helper(0,self.n-1,0,j)+
                self.helper(0,i,j+1,self.m-1)+
                self.helper(i+1,self.n-1,j+1,self.m-1)
                )

                # Left up, left bottom, right strip
                res = min(res,
                self.helper(0,i,0,j)+
                self.helper(i+1,self.n-1,0,j)+
                self.helper(0,self.n-1,j+1,self.m-1)
                )
        return res