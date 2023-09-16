class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack=[]
        for ch in s:
            if ch!='*':
                stack.append(ch)
            else:
                stack.pop()
            
        s=''.join(str(x) for x in stack)
        return s


        