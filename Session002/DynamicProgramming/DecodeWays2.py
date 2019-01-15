class Solution(object):
    """
    https://leetcode.com/problems/decode-ways/description/
    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo=[0]*(len(s)+1)
        memo[0]=1
        memo[1]=1 if s[0]!='0' and int(s[0])<=9 else 0
        for i in range(len(s)+1):
            if int(s[i-1:i])>0 and int(s[i-1:i])<=9:
                memo[i]+=memo[i-1]
            if s[i-2:i][0]!='0' and int(s[i-2:i])<=26:
                memo[i]+=memo[i-2]
        return memo[-1]



    def numDecodings2(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo=[0]*(len(s)+1)
        memo[0]=1
        memo[1]=(1 if int(s[0])>0 and int(s[0])<=9 else 0)

        for i in range(2, len(s)+1):
            if int(s[i-1:i])>0 and int(s[i-1:i])<=9:
                memo[i]+=memo[i-1]
            if s[i-2:i][0]!='0' and int(s[i-2:i])<=26:
                memo[i]+=memo[i-2]
        return memo[-1]

 
    def numDecodings3(self, s):
        """
        :type s: str
        :rtype: int
        """
        memo=[0]*(len(s)+1)
        memo[0]=1
        memo[1]=1 if s[0]!='0' and int(s[0])<=9 else 0

        for i in range(2, len(s)+1):
            if int(s[i-1:i])>0 and int(s[i-1:i])<=9:
                memo[i]+=memo[i-1]
            if s[i-2:i][0]!='0' and int(s[i-2:i])<=26:
                memo[i]+=memo[i-2]
        return memo[-1]







    def numDecodings4(self, s):
        memo=[0]*(len(s)+1)
        memo[0]=1
        memo[1]=(1 if s[0]!='0' and int(s[0])<=9 else 0)

        for i in range(2,len(s)+1):
            if int(s[i-1:i])>0 and int(s[i-1:i])<=9:
                memo[i]+=memo[i-1]
            if s[i-2:i][0]!='0' and int(s[i-2:i])<=26:
                memo[i]+=memo[i-2]
        return memo[-1]

        
        
            










if __name__ == "__main__":
    c=Solution()
    print(c.numDecodings("10"))
