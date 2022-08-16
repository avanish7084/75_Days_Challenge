class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        n_r=len(grid)
        n_c=len(grid[0])
        ans=list(range(n_c))
        for r in range(n_r):
            for i in range(n_c):
                c=ans[i]
                if c==-1:
                    continue
                c_next=c+grid[r][c]
                if c_next<0 or c_next>=n_c or grid[r][c_next]==-grid[r][c]:
                    ans[i]=-1
                    continue
                ans[i]+=grid[r][c]
        return ans
