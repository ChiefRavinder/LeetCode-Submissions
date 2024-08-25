class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if haystack==needle:
            return 0

        low=0
        if len(needle)==1 and haystack[0]==needle:
            return 0


        if len(needle)==1:
            high=1
        else:
            high=len(needle)-1

        i=0
        while high <= len(haystack):
            if haystack[low:(high+1)]==needle:
                return i
            else:
                i+=1
                low+=1
                high+=1
        return (-1)

