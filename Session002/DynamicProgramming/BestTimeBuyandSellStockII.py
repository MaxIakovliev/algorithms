class Solution(object):
    def maxProfit(self, a):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(a)==0:
            return 0
        minVal=a[0]
        summary=0
        curMax=0
        for i in range(1,len(a)):
            if a[i]>minVal and a[i]>a[i-1]:
                curMax=max(curMax, a[i]-minVal)
            else:
                summary+=curMax
                curMax=0
                minVal=a[i]
        summary+=curMax
        return summary
if __name__=="__main__":
    c=Solution()
    print(c.maxProfit([7,1,5,3,6,4])) # 7
    print(c.maxProfit([1,2,3,4,5])) #4
    print(c.maxProfit([7,6,4,3,1])) #0
    print(c.maxProfit([6,1,3,2,4,7])) #7
            
        