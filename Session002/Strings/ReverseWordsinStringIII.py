class Solution:
    """
    https://leetcode.com/problems/reverse-words-in-a-string-iii/description/
    """
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res=[]
        idx=0
        for c in s:
            if c==" ":
                res.append(' ')
                idx=len(res)
            else:
                res.insert(idx,c)
        return "".join(res)

if __name__=="__main__":
    c=Solution()
    print("'{0}'".format(c.reverseWords("hello world 123")))
