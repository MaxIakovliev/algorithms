class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        lo=1
        hi=num
        while lo<=hi:
            mid=(int)((lo+hi)/2)
            t=mid*mid
            if t==num:
                return True
            elif t>num:
                hi=mid-1
            else:
                lo=mid+1
        return False
if __name__=="__main__":
    c=Solution()
    for i in range(17):
        print(str(i)+"="+ str(c.isPerfectSquare(i)))
    # print(c.isPerfectSquare(9))
