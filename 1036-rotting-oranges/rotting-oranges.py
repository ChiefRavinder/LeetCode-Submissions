class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        vis=[[0]*n for _ in range(m)]
        new=[[0]*n for _ in range(m)]
        time=0
        for i in range(m):
            for j in range(n):
                new[i][j]=grid[i][j]
                    
        q=[]
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    vis[i][j]=1
                    q.append((i,j,0))
        while q:
            row=q[0][0]
            col=q[0][1]
            t=q[0][2]
            q.pop(0)
            delrow=[0,1,0,-1]
            delcol=[1,0,-1,0]
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if 0<=nrow<m and 0<=ncol<n and vis[nrow][ncol]!=1 and grid[nrow][ncol]==1 and new[nrow][ncol]!=2:
                    vis[nrow][ncol]=1
                    new[nrow][ncol]=2
                    nt=t+1
                    q.append((nrow,ncol,nt))
                    time=max(time,nt)
        for i in range(m):
            for j in range(n):
                if new[i][j]==1:
                    return -1
        return time
        
        