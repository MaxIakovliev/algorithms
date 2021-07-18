class Solution:
    """
    https://leetcode.com/problems/implement-strstr/description/
    """
    def strStr(self, a, b):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if len(a)==0  and len(b)==0:
            return 0
        if b=="":
            return 0
        start=0
        end=len(b)-1
        idx=0
        if len(b)==1:
            for i in range(len(a)):
                if a[i]==b[0]:
                    return i
            return -1

        while idx<len(a):
            start=0
            end=len(b)-1
            found=True
            while start<=end:
                if idx+end>len(a)-1 or idx+start>len(a)-1:
                    return -1
                if a[idx+start]!=b[start] or a[idx+end]!=b[end]:
                    idx+=1#len(b)
                    found=False
                    break
                start+=1
                end-=1
            if found:
                return idx
        return -1

if __name__=="__main__":
    c=Solution()
    print(c.strStr('hello','ll'))
    print(c.strStr('abcbac','bcb'))
    print(c.strStr('abcbac','becb'))
    print(c.strStr('abcbac',''))
    print(c.strStr('babb','bbb'))
                
        