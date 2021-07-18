class Solution:
    """
    https://leetcode.com/problems/word-break/
    solution:
    https://leetcode.com/problems/word-break/discuss/43790/Java-implementation-using-DP-in-two-ways
    """
    def wordBreak(self, s: str, wordDict: 'List[str]') -> bool:
        dp=[False for _ in range(len(s)+1)]
        dp[0]=True
        for i in range(1, len(s)+1):
            for j in range(i):
                if dp[j] and s[j:i] in wordDict:
                    dp[i]=True
                    break
        return dp[-1]

        