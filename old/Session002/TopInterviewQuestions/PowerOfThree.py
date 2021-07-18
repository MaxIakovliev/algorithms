class Solution:
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n<1:
            return False
        while n!=1:
            if n%3!=0:
                return False
            n/=3
        return True
if __name__=="__main__":
    c=Solution()
    print(c.isPowerOfThree(27))
    print(c.isPowerOfThree(9))
    print(c.isPowerOfThree(45))
 