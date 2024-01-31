from collections import deque

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        deq=deque()
        out=[0]*len(temperatures)

        for i in range(len(temperatures)-1,-1,-1):
            if not deq:
                deq.appendleft(i)
                out[i]=0
            else:
                while deq and temperatures[i]>=temperatures[deq[0]]:
                    deq.popleft()

                if not deq:
                    out[i]=0
                else:
                    out[i]=deq[0]-i
                deq.appendleft(i)

        return out

        