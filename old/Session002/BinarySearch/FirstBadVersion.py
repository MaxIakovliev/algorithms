# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    pass

class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        lo=1
        hi=n
        while lo<=hi:
            mid=(lo+hi)//2
            if isBadVersion(mid)==True:
                if isBadVersion(mid-1)==False:
                    return mid
                else:
                    hi=mid-1
            else:
                lo=mid+1


                