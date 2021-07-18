class Solution:
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        res=0
        for i in range(len(s)):
            res+=self.tryExtend(s,i,i)
            res+=self.tryExtend(s,i, i+1)
        return res

    def tryExtend(self, s, start,end):
        count=0
        while start>=0 and end<len(s) and s[start]==s[end]:
            count+=1
            start-=1
            end+=1
        return count
if __name__=="__main__":
    c=Solution()
    print(c.countSubstrings("abc"))
