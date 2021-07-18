class Solution:
    """
    https://leetcode.com/problems/decode-ways/description/
    A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given an encoded message containing digits, determine the total number of ways to decode it.
    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        if s is None or len(s)==0:
            return 0
        n=len(s)
        dp=[0]*(n+1)
        dp[0] = 1
        dp[1]=1 if s[0]!='0' else 0
        for i in range(2,n+1):
            first=int(s[i-1:i])
            second=int(s[i-2:i])
            if(first>=1 and first<=9):
                dp[i]+=dp[i-1]
            if second>=10 and second<=26:
                dp[i]+=dp[i-2]
        return dp[n]


    def numDecodings2(self, s):
        memo=[0]*(len(s)+1)
        memo[0]=1
        memo[1]=(1 if int(s[0])>0 and int(s[0])<=9 else 0)
        for i in range(2, len(s)):
            if int(s[i-1:i])>0 and int(s[i-1:i])<=9:
                memo[i]+=memo[i-1]
            if s[i-2:i][0]!='0' and int(s[i-2:i])<=26:
                memo[i]+=memo[i-2]
        return memo[-1]


    def numDecodings3(self, s):
        dp=[0]*(len(s)+1)
        dp[0]=1
        dp[1]=(1 if s[0]!='0' and int(s[0])<9 else 0)
        for i in range(2, len(s)):
            if s[i-1]!='0' and int(s[i-1])<=9:
                dp[i]=dp[i-1]
            if s[i-2:i][0]!='0' and int(s[i-2:i])<=26:
                dp[i]+=dp[i-1]
        return dp[-1]
       