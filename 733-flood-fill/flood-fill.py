class Solution:
    def dfs(self,r,c,img,new,old_color,new_color,n,m):
        new[r][c]=new_color
        dr=[-1,0,1,0]
        dc=[0,1,0,-1]
        for i in range(4):
            nr=r+dr[i]
            nc=c+dc[i]
            if 0<=nr<n and 0<=nc<m and img[nr][nc]==old_color and new[nr][nc]!=new_color:
                self.dfs(nr,nc,img,new,old_color,new_color,n,m)

    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        n=len(image)
        m=len(image[0])
        new=[[0]*m for _ in range(n)]
        in_color=image[sr][sc]
        for i in range(n):
            for j in range(m):
                new[i][j]=image[i][j]
        self.dfs(sr,sc,image,new,in_color,color,n,m)
        return new

        

        