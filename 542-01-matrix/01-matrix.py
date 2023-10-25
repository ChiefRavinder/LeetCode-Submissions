class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m=len(mat)
        n=len(mat[0])
        vis=[[0]*n for _ in range(m)]
        dis=[[0]*n for _ in range(m)]
        q=[]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    vis[i][j]==1
                    q.append((i,j,0))
        while q:
            row=q[0][0]
            col=q[0][1]
            d=q[0][2]
            q.pop(0)
            delrow=[0,1,-1,0]
            delcol=[1,0,0,-1]
            for i in range(4):
                newrow=row+delrow[i]
                newcol=col+delcol[i]
                if 0<=newrow<m and 0<=newcol<n and mat[newrow][newcol]==1 and vis[newrow][newcol]!=1:
                    vis[newrow][newcol]=1
                    dis[newrow][newcol]=d+1
                    q.append((newrow,newcol,d+1))
        return dis
        