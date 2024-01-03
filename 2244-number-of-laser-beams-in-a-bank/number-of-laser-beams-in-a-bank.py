class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        poc=0
        ans=0

        for i in (bank):
            coc=0
            for j in i:
                if j =='1':
                    coc+=1
            if coc>0:
                ans+=coc*poc
                poc=coc
        return ans