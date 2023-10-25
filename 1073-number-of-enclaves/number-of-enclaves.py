class Solution:
    def dfs(self,r,c,vis,grid,m,n):
        vis[r][c]=1
        delr=[0,1,-1,0]

        delc=[1,0,0,-1]
        for i in range(4):
            nr=r+delr[i]
            nc=c+delc[i]
            if 0<=nr<m and 0<=nc<n and vis[nr][nc]!=1 and grid[nr][nc]==1:
                vis[nr][nc]=1
                self.dfs(nr,nc,vis,grid,m,n)

    def numEnclaves(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        vis=[[0]*n for _ in range(m)]
        for i in range(m):
            if grid[i][0]==1:
                vis[i][0]=1
                self.dfs(i,0,vis,grid,m,n)
            if grid[i][n-1]==1:
                vis[i][n-1]=1
                self.dfs(i,n-1,vis,grid,m,n)
        for j in range(n):
            if grid[0][j]==1:
                vis[0][j]=1
                self.dfs(0,j,vis,grid,m,n)
            if grid[m-1][j]==1:
                vis[m-1][j]=1
                self.dfs(m-1,j,vis,grid,m,n)
        cnt=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and vis[i][j]!=1:
                    cnt+=1
        return cnt
        