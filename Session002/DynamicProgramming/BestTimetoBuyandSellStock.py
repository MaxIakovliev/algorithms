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
if __name__=="__main__":
    c=Solution()
    print(c.maxProfit([7,1,5,3,6,4]))
    print(c.maxProfit([7,6,4,3,1]))
        
        
