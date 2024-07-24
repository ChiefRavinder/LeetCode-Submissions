from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj=[[] for _ in range(numCourses)]
        for i in prerequisites:
            adj[i[1]].append(i[0])
        V=numCourses
        inDegree=[0]*V
        q=deque()
        vis=[0]*V
        out=[]
        for i in range(V):
            for j in adj[i]:
                inDegree[j]+=1
        for i in range(V):
            if inDegree[i]==0:
                q.append(i)
        while q:
            node=q.popleft()
            out.append(node)
            # vis(node)=1
            for i in adj[node]:
                inDegree[i]-=1
                # vis[i]=1
                if inDegree[i]==0:
                    q.append(i)
        return len(out)==V
        