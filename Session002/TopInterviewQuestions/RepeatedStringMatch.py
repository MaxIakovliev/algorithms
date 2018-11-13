class Solution:
    """
    https://leetcode.com/problems/repeated-string-match/description/
    """
    def repeatedStringMatch(self, a, b):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        multiplier=1
        
        if len(b)>len(a):
            multiplier=len(b)//len(a)
            if len(b)%len(a)!=0:
                multiplier+=1

        s="".join([a]*multiplier)
        start=0
        end=len(b)-1
        if b in s:
            return multiplier
        s+=a
        multiplier+=1
        if b in s:
            return multiplier
        return -1

if __name__=="__main__":
    c=Solution()
    print(c.repeatedStringMatch("abcd","cdabcdab"))


            

        
            
        