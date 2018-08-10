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






if __name__=="__main__":
    c=Solution()
    print(c.maxProfit3([7,1,5,3,6,4])) #5
    print(c.maxProfit3([7,6,4,3,1])) #0
    print(c.maxProfit3([1])) #0
        
        
