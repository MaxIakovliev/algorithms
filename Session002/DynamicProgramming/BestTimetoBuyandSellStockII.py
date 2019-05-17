class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/
    
    solution:
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/discuss/266008/C%2B%2B-DP-O(n)
    """
    def maxProfit(self, prices: 'List[int]') -> int:
        buy1=float('-inf')
        buy2=float('-inf')
        sell1=0
        sell2=0
        for i in range(len(prices)):
            buy1=max(buy1, -prices[i])
            sell1=max(sell1,prices[i]+buy1)
            buy2=max(buy2, sell1-prices[i])
            sell2=max(sell2, prices[i]+ buy2)
        return sell2
        