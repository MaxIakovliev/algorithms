class Solution:
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        d={}
        for c in s:
            if c not in d:
                d[c]=1
            else:
                d[c]+=1
        for c in t:
            if c not in d:
                return c
            else:
                d[c]-=1
                if d[c]==0:
                    del d[c]
            
    def findTheDifference2(self, s, t):
        res=ord(s[0])
        for i in range(1, len(s)):
            res^=ord(s[i])
        for i in range(len(t)):
            res^=ord(t[i])
        return chr(res)

            
        
    

if __name__=="__main__":
    c=Solution()
    print(c.findTheDifference2("abc","aebc"))
    print(c.findTheDifference2("aa","aab"))
