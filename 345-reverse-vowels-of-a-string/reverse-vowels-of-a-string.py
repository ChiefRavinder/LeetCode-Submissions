class Solution:
    def reverseVowels(self, s: str) -> str:
        # vow=[i for i in s if i in 'aeiou']
        # vow=vow[::-1]
        # ind=0
        # for i in range(len(s)):
        #     if s[i] in 'aeiou':
        #         tmp=""
        #         tmo=vow[ind]
        #         s[i]=tmp
        #         ind+=1
        # return s
        s=list(s)
        start=0
        end=(len(s))-1
        while start<end:
            if s[start] in 'aeiouAEIOU' and s[end] in 'aeiouAEIOU':
                s[start],s[end]=s[end],s[start]
                start+=1
                end-=1
            elif s[start] not in 'aeiouAEIOU' and s[end] in 'aeiouAEIOU':
                start+=1
            elif s[start] in 'aeiouAEIOU' and s[end] not in 'aeiouAEIOU':
                end-=1
            else:
                start+=1
                end-=1
        
        s=''.join(s)
        return s    






        