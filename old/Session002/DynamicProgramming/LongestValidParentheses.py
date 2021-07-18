class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        dp=[0]*len(s)
        res=0
        leftCount=0
        for i in range(len(s)):
            if s[i]=='(':
                leftCount+=1
            elif s[i]==')' and leftCount>0:
                dp[i]=dp[i-1]+2
                dp[i]+=(dp[i-dp[i]] if i-dp[i]>=0 else 0)
                res=max(res,dp[i])
                leftCount-=1
        return res