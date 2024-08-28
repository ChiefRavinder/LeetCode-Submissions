class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        def f(i,j,shape,dp):
            if i==len(shape)-1:
                return shape[i][j]
            if dp[i][j]!=-1:
                return dp[i][j]
            fs=shape[i][j]+f(i+1,j+1,shape,dp)
            ss=shape[i][j]+f(i+1,j,shape,dp)
            dp[i][j]=min(fs,ss)
            return min(fs,ss)
        m=len(triangle)
        dp=[[-1]*m for _ in range(m)]
        return f(0,0,triangle,dp)
        