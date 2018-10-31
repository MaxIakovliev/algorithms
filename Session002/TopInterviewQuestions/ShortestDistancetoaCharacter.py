class Solution:
    """
    https://leetcode.com/problems/shortest-distance-to-a-character/description/
    """
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        cx=[]
        for i in range(len(S)):
            if S[i]==C:
                cx.append(i)
        
        curi=0
        res=[0]*len(S)
        for i in range(len(S)):
            if curi+1<len(cx):
                res[i]=min(abs(i-cx[curi]), abs(i-cx[curi+1]))
            else:
                res[i]=abs(abs(i-cx[curi]))
            if curi+1<len(cx) and i==cx[curi+1]:
                curi+=1
        return res
if __name__=="__main__":
    c=Solution()
    print(c.shortestToChar('loveleetcode','e'))


        