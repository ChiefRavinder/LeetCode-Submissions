from collections import deque
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        color=[-1]*len(graph)
        def bfs(start,graph,color):
            q=deque()
            color[start]=0
            q.append(start)
            while(len(q)!=0):
                element=q.popleft()
                for ele in graph[element]:
                    if(color[ele]==-1):
                        if(color[element]==0):
                            color[ele]=1
                            q.append(ele)
                        else:
                            color[ele]=0
                            q.append(ele)
                    else:
                        if(color[ele]==color[element]):
                            return False 
            return True
        for i in range(len(graph)):
            if(color[i]==-1):
                if(bfs(i,graph,color)==False):
                    return False
        return True