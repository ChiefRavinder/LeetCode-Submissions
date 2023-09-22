class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        
        if s=='':
            return True
        i=0
        
        for l in t:
            k=s[i]
            if l==k:
                i+=1
            if i==len(s):
                break
        
        return i==len(s)
        

        

        