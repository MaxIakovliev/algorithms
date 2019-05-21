class Solution(object):
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

    solution:
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75928/Share-my-DP-solution-(By-State-Machine-Thinking)
    """
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<=1:
            return 0
        s0=[0 for _ in range(n)]
        s1=[0 for _ in range(n)]
        s2=[0 for _ in range(n)]
        
        s1[0]=-prices[0]
        s0[0]=0
        s2[0]=float('-inf')
        for i in range(1, n):
            s0[i]=max(s0[i-1],s2[i-1])
            s1[i]=max(s1[i-1],s0[i-1]-prices[i])
            s2[i]=s1[i-1]+prices[i]
        return max(s0[-1],s2[-1])
        