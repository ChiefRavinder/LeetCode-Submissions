class Solution:
    def reverseWords(self, s: str) -> str:
        l = s.split()
        l=l[::-1]
        s=' '.join(str(x) for x in l)
        return s