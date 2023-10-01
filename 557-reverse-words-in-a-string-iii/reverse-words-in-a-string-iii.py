class Solution:
    def reverseWords(self, s: str) -> str:
        out=s.split(' ')
        for i in range(len(out)):
            temp=out[i]
            out[i]=temp[::-1]
        return " ".join(out)

        