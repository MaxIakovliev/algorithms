class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        convert from:https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/discuss/108871/2-solutions-2-states-DP-solutions-clear-explanation!
        """
        days=len(prices)
        if days<=1:
            return 0
        
        buy=[0 for _ in range(days)]
        sell=[0 for _ in range(days)]
        buy[0]=-prices[0]
        for i in range(1, days):
            buy[i]=max(buy[i-1], sell[i-1]-prices[i])
            sell[i]=max(sell[i-1], buy[i-1]+prices[i]-fee)
        return sell[days-1]