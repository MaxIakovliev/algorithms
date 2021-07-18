class Solution:
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        res={}
        for i in range(len(s)):
            if s[i] in res:
                res[s[i]]=float('inf')
            else:
                res[s[i]]=i
        
        m=float('inf')
        for k,v in res.items():
            m=min(m,v)
        if m==float('inf'):
            return -1
        return m
if __name__ =="__main__":
    c=Solution()
    print(c.firstUniqChar("laeetlcode"))
    print(c.firstUniqChar("loveleetcode"))
    print(c.firstUniqChar("aa"))

    
