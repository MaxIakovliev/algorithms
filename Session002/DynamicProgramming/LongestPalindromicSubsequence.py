class Solution:
    """
    https://leetcode.com/problems/longest-palindromic-subsequence/
    solution:
    1.https://leetcode.com/problems/longest-palindromic-subsequence/discuss/195957/Python-easy-to-understand-O(n2)-solution.
    """
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        dp=[[1 for _ in range(n)] for _ in range(n)]

        # Single character Palindrome
        for i in range(n):
            dp[i][i]=1
        
         # Adjacent 2 character Palindrome
        for i in range(n-1):
            if s[i]==s[i+1]:
                dp[i][i+1]=2
        
        # Palindromes between i & j
        for i in range(n-3,-1,-1):
            for j in range(i+2,n):
                if s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]+2
                else:
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])

        return dp[0][-1]


    """
    solution:
    https://leetcode.com/problems/longest-palindromic-subsequence/discuss/196687/Yet-another-Python3-solution%3A-DP-O(n2)-time-O(n)-space-%3A)
    """
    def longestPalindromeSubseq2(self, s: str) -> int:
        n=len(s)
        if n<2:
            return n
        prev=[0]*n
        cur=[1]*n
        for ln in range(2,n+1):
            nxt=[0]*n
            for start in range(n-ln+1):
                end=start+ln-1
                if s[start]==s[end]:
                    nxt[start]=prev[start+1]+2
                else:
                    nxt[start]=max(cur[start+1], cur[start])
            cur, prev, =nxt, cur
        return cur[0]







