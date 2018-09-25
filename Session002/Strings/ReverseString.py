class Solution:
    """
    https://leetcode.com/problems/reverse-string/description/
    """
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        i=len(s)-1
        while (i>=0):
            res.append(s[i])
            i-=1
        return "".join(res)