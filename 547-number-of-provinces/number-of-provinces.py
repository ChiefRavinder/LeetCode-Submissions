class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        def dfs(node,adj,vis):
            vis[node]=1
            for i in adj[node]:
                if vis[i]!=1:
                    dfs(i,adj,vis)

        adj=[[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
        vis=[0]*len(isConnected)
        cnt=0
        for i in range(len(vis)):
            if vis[i]!=1:
                cnt+=1
                dfs(i,adj,vis)
        return cnt


        