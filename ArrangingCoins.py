class Solution(object):
    def arrangeCoins(self, n):
        """
        :type n: int
        :rtype: int
        """
        count=1
        while n-count>=0:
            n=n-count
            count+=1
        return count-1

if __name__ =="__main__":
    c=Solution()
    print(c.arrangeCoins(5))