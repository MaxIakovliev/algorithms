class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n=len(prices)
        if n<=1:
            return 0
        res=0
        if k>= n//2:
            for i in range(1,n):
                if prices[i]>prices[i-1]:
                    res+=(prices[i]-prices[i-1])
            return res
        
        dp=[[0]*n]*(k+1)
        for i in range(1, k+1):
            localMax=dp[i-1][0]-prices[0]
            for j in range(1, n):
                dp[i][j]=max(dp[i][j-1],prices[j]+localMax)
                localMax=max(localMax, dp[i-1][j]-prices[j])
        return dp[k][n-1]

if __name__=="__main__":
    c=Solution()
    # print(c.maxProfit(2, [3,2,6,5,0,3]))#7
    print(c.maxProfit(2, [3,3,5,0,0,3,1,4])) #6 not working


        
        