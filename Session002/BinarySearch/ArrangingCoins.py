class Solution:
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        step=1
        count=0
        while n>0:
            n=n-step
            step+=1
            count+=1
        if n<0:
            return count-1
        return count
if __name__ =="__main__":
    c=Solution()
    print(c.arrangeCoins(5))
    print(c.arrangeCoins(8))
