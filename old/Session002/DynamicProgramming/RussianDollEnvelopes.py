class Solution(object):
    """
    https://leetcode.com/problems/russian-doll-envelopes/
    """
    def maxEnvelopes(self, envelopes):
        """
        :type envelopes: List[List[int]]
        :rtype: int
        """
        if not envelopes:
            return 0
        envelopes.sort()
        n=len(envelopes)
        dp=[1 for _ in range(n)]
        res=0
        for i in range(n):
            for j in range(i):
                if envelopes[i][0]>envelopes[j][0] and envelopes[i][1]>envelopes[j][1]:
                    dp[i]=max(dp[i], dp[j]+1)
            res=max(res, dp[i])
        return res
        