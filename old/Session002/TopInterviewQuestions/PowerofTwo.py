
import math
class Solution:
    def isPowerOfTwo1(self, n):
        """
        :type n: int
        :rtype: bool
        """

        if n==0 or n<0:
            return False
        if n <0:
            n=abs(n)
        while n!=1:
            if n%2!=0:
                return False
            n/=2
        return True



if __name__=="__main__":
    c=Solution()
    for n in range(16385-10, 16386):
        print(c.isPowerOfTwo1(n))
