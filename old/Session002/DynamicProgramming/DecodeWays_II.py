class Solution:
    """
    https://leetcode.com/problems/decode-ways-ii/description/

    этот какая то дичь: https://leetcode.com/problems/decode-ways-ii/discuss/105262/Python-6-lines-DP-solution

    """
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        one = {str(i): 1 for i in range(1, 10)}
        one.update({'*': 9, '0': 0})

        two = {str(i): 1 for i in range(10, 27)}
        two.update({'*' + str(i): 2 if i <= 6 else 1 for i in range(10)})
        two.update({'1*': 9, '2*': 6, '**': 15})
        dp = (1, one.get(s[:1], 0))

        for i in range(1, len(s)):
            dp = (dp[1], (one.get(s[i]) * dp[1] + two.get(s[i - 1: i + 1], 0) * dp[0]) % 1000000007)

        return dp[-1]

             
