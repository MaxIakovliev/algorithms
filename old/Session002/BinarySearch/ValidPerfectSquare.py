class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num==1:
            return True
        lo=1
        hi=num-1
        while lo<hi:
            mid=(int)((lo+hi)/2)
            d=mid*mid
            if d==num:
                return True
            elif d>num:
                hi=mid
            else:
                lo=mid+1
        return False 

if __name__ =="__main__":
    c=Solution()
    print(c.isPerfectSquare(16))
    print(c.isPerfectSquare(14))
    print(c.isPerfectSquare(4))
    print(c.isPerfectSquare(5))
    print(c.isPerfectSquare(1))