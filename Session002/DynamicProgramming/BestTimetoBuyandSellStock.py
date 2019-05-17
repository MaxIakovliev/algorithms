class Solution:
    """
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/description/

    """

    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minVal=prices[0]
        maxVal=0
        for i in range(len(prices)):
            if minVal<prices[i]:
                maxVal=max(maxVal, prices[i]-minVal)
            else:
                minVal=prices[i]
        return maxVal



    def maxProfit2(self, a):
        if len(a)==0:
            return 0
        minVal=a[0]
        maxVal=0
        for i in range(len(a)):
            if a[i]>minVal:
                maxVal=max(maxVal, a[i]-minVal)
            else:
                minVal=a[i]
        return maxVal

    
    def maxProfit3(self, a):
        t1=0
        t2=float("-inf")
        for price in a:
            t1=max(t1,t2+price)
            t2=max(t2,-price)
        return t1

    #DP solution
    """
    solution:
    https://leetcode.com/problems/best-time-to-buy-and-sell-stock/discuss/39112/Why-is-this-problem-tagged-with-"Dynamic-programming"/36893
    """
    def maxProfit4(self, prices):
        if prices is None or len(prices)==0:
            return 0        
        dp=[0 for _ in range(len(prices))]
        min_price=prices[0]
        for i in range(1,len(prices)):
            dp[i]=max(dp[i-1], prices[i]-min_price)
            min_price=min(min_price,prices[i])
        return dp[-1]








if __name__=="__main__":
    c=Solution()
    print(c.maxProfit3([7,1,5,3,6,4])) #5
    print(c.maxProfit3([7,6,4,3,1])) #0
    print(c.maxProfit3([1])) #0
        
        
