class Solution(object):
    """
    https://leetcode.com/problems/wildcard-matching/description/
    great explanation: https://www.youtube.com/watch?v=3ZDZ-N0EPV0
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        memo[0][0]=True
        for i in range(1, len(p)+1):
            if p[i-1]=='*':
                if i>0:
                    memo[0][i]=memo[0][i-1]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1]=='?':
                    memo[i][j]=memo[i-1][j-1]
                elif p[j-1]=='*':
                    memo[i][j]=memo[i][j-1] or memo[i-1][j]
                else:
                    memo[i][j]=memo[i-1][j-1]==True and s[i-1]==p[j-1]
        return memo[len(s)][len(p)]



    def isMatch2(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo=[[0 for i in range(len(p)+1)] for j in range(len(s)+1)]
        memo[0][0]=True
        for i in range(1,len(p)+1):
            if p[i-1]=='*':
                if i>0:
                    memo[0][i]=memo[0][i-1]
        
        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j-1]=='?':
                    memo[i][j]=memo[i-1][j-1]
                elif p[j-1]=='*':
                    memo[i][j]=memo[i][j-1] or memo[i-1][j]
                else:
                    memo[i][j]=memo[i-1][j-1]==True and s[i-1]==p[j-1]
        return memo[-1][-1]





if __name__=="__main__":
    c=Solution()
    print(c.isMatch2("aa","a"))#false
    print(c.isMatch2("aa","*"))#true
    print(c.isMatch2("cb","?a"))#false
    print(c.isMatch2("adceb","*a*b"))#true
    print(c.isMatch2("acdcb","a*c?b"))#false

        