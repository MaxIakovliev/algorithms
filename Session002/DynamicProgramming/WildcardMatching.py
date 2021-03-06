class Solution(object):
    """
    https://leetcode.com/problems/wildcard-matching/description/
    great explanation: https://www.youtube.com/watch?v=3ZDZ-N0EPV0


Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.
Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.
Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".
Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false

    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        memo[0][0]=True
        for j in range(len(p)+1):
            if p[j-1]=="*":
                if j>0:
                    memo[0][j]=memo[0][j-1]
 

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1]=='?':
                    memo[i][j]=memo[i-1][j-1]
                elif p[j-1]=='*':
                    memo[i][j]=memo[i-1][j] or memo[i][j-1] 
                else:
                    memo[i][j]=memo[i-1][j-1] and s[i-1]==p[j-1]
        return memo[len(s)][len(p)]

    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """        
        dp = [[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        dp[0][0] = True
        for i in range(1,len(p)+1):
            if p[i-1] == '*':
                if i >= 1:
                    dp[0][i] = dp[0][i-1]
        for i in range(1,len(s)+1):
            for j in range(1,len(p)+1):
                if p[j-1]=='?':
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1]=='*':
                    dp[i][j] = dp[i][j-1] or dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j-1] and s[i-1] == p[j-1]
        return dp[len(s)][len(p)]        
if __name__=="__main__":
    c=Solution()
    print(c.isMatch("aa","a"))#false
    print(c.isMatch("aa","*"))#true
    print(c.isMatch("cb","?a"))#false
    print(c.isMatch("adceb","*a*b"))#true
    print(c.isMatch("acdcb","a*c?b"))#false

        