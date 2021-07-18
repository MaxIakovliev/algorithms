class Solution:
    """
    https://leetcode.com/problems/regular-expression-matching/description/
    good explanation here:
    https://leetcode.com/problems/regular-expression-matching/discuss/5723/My-DP-approach-in-Python-with-comments-and-unittest
    """
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        memo=[[False for i in range(len(p)+1)] for j in range(len(s)+1)]
        memo[0][0]=True
        for j in range(2,len(p)+1):
            memo[0][j]=p[j-1]=="*" and memo[0][j-2]

        for i in range(1, len(s)+1):
            for j in range(1, len(p)+1):
                if p[j - 1] != "*":
                    memo[i][j] = memo[i - 1][j - 1] and  (p[j - 1] == s[i - 1] or p[j - 1] == '.')
                else:
                    memo[i][j] = memo[i][j-2] or memo[i][j-1]
                    if p[j - 2] == s[i - 1] or p[j - 2] == '.':
                        memo[i][j] |= memo[i-1][j]
        return memo[-1][-1]

if __name__=="__main__":
    c=Solution()
    print(c.isMatch("mississippi","mis*is*p*."))#false
    print(c.isMatch("aa","a"))#false
    print(c.isMatch("aa","a*"))#true
    print(c.isMatch("ab",".*"))#true
    print(c.isMatch("aab","c*a*b"))#true