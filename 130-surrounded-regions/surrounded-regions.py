class Solution:
    def dfs(self,r,c,vis,board,m,n):
        vis[r][c]=1
        delr=[0,1,-1,0]
        delc=[1,0,0,-1]
        for i in range(4):
            nr=r+delr[i]
            nc=c+delc[i]
            if 0<=nr<m and 0<=nc<n and board[nr][nc]=='O' and vis[nr][nc]!=1:
                vis[nr][nc]=1
                self.dfs(nr,nc,vis,board,m,n)

        
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        vis=[[0]*n for _ in range(m)]
        for i in range(n):
            if board[0][i]=='O':
                vis[0][i]=1
                self.dfs(0,i,vis,board,m,n)
            if board[m-1][i]=='O':
                vis[m-1][i]=1
                self.dfs(m-1,i,vis,board,m,n)
        for i in range(m):
            if board[i][0]=='O':
                vis[i][0]=1
                self.dfs(i,0,vis,board,m,n)
            if board[i][n-1]=='O':
                vis[i][n-1]=1
                self.dfs(i,n-1,vis,board,m,n)
        for i in range(m):
            for j in range(n):
                if board[i][j]=='O' and vis[i][j]!=1:
                   board[i][j]='X'
        


        