# The guess API is already defined for you.
# @param num, your guess
# @return -1 if my number is lower, 1 if my number is higher, otherwise return 0
# def guess(num):
def guess(num):
    if num==2:
        return 0
    elif num>2:
        return -1
    else:
        return 1


class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==1:
            return n

        lo=0
        hi=n
        while lo<=hi:
            mid=(int)((lo+hi)/2)
            r=guess(mid)
            if r==0:
                return mid
            elif r<0:
                hi=mid
            else:
                lo=mid+1
        return -1 

if __name__ =="__main__":
    c=Solution()
    print(c.guessNumber(2))