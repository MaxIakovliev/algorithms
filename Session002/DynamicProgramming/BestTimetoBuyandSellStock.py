class Solution:
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






if __name__=="__main__":
    c=Solution()
    print(c.maxProfit2([7,1,5,3,6,4]))
    print(c.maxProfit2([7,6,4,3,1]))
    print(c.maxProfit2([1]))
        
        
