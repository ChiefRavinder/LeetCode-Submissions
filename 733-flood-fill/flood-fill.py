class Solution:
    def dfs(self,image,new,sr,sc,color,m,n,pre_col,vis):
        new[sr][sc]=color
        dr=[0,1,-1,0]
        dc=[1,0,0,-1]
        for i in range(4):
            newr=sr+dr[i]
            newc=sc+dc[i]
            if 0<=newr<m and 0<=newc<n and vis[newr][newc]!=1 and image[newr][newc]==pre_col:
                vis[newr][newc]=1
                new[newr][newc]=color
                self.dfs(image,new,newr,newc,color,m,n,pre_col,vis)
                
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        pre_col=image[sr][sc]
        m=len(image)
        n=len(image[0])
        new=[[0]*n for _ in range(m)]
        vis=[[0]*n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                new[i][j]=image[i][j]
        self.dfs(image,new,sr,sc,color,m,n,pre_col,vis)
        return new

        

        