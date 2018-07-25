class Solution:
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        lo=0
        hi=x
        if x==1:
            return x
        while lo<hi:
            mid=(int)((lo+hi)/2)
            r=mid*mid
            if r==x:
                return mid
            elif r<x and (mid+1)*(mid+1)>x:
                return mid
            elif r>x:
                hi=mid
            else:
                lo=mid+1
        return 0

if __name__ =="__main__":
    c=Solution()
    print(c.mySqrt(4))
    print(c.mySqrt(8))
    print(c.mySqrt(10))