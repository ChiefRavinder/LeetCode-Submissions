class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        rott=[[0]*n for _ in range(m)]
        time=0
        for i in range(m):
            for j in range(n):
                rott[i][j]=grid[i][j]
        q=[]
        vis=[[0]*n for _ in range(m)] 
        for i in range(m):
            for j in range(n):
                if rott[i][j]==2:
                    vis[i][j]=1
                    q.append((i,j,0))
        while q:
            node=q.pop(0)
            r=node[0]
            c=node[1]
            t=node[2]
            dr=[1,0,-1,0]
            dc=[0,1,0,-1]
            for k in range(4):
                nr=dr[k]+r
                nc=dc[k]+c
                if 0<=nr<m and 0<=nc<n and vis[nr][nc]!=1 and rott[nr][nc]==1:
                    vis[nr][nc]=1
                    rott[nr][nc]=2
                    nt=t+1
                    q.append((nr,nc,nt))
                    time=max(time,nt)
        for i in range(m):
            for j in range(n):
                if rott[i][j]==1:
                    return -1
        return time
                    
