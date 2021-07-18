class Solution(object):
    """
    https://leetcode.com/problems/monotonic-array/
    """
    def isMonotonic(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        way=0
        for i in range(len(A)-1):
            if A[i]<A[i+1] and way==0:
                way=-1
            elif A[i]>A[i+1] and way<0:
                return False
            elif A[i]>A[i+1] and way==0:
                way=1
            elif A[i]<A[i+1] and way>0:
                return False
        return True

    def isMonotonic2(self, A):
        """
        :type A: List[int]
        :rtype: bool
        """
        inc,dec=True,True
        for i in range(len(A)-1):
            inc&=A[i]<=A[i+1]
            dec&=A[i]>=A[i+1]
        return inc or dec

if __name__=="__main__":
    c=Solution()
    print(c.isMonotonic2( [1,2,2,3]))#True
    print(c.isMonotonic2( [6,5,4,4]))#True
    print(c.isMonotonic2( [1,3,2]))#False
    print(c.isMonotonic2( [1,2,4,5]))#True
    print(c.isMonotonic2( [1,1,1,1]))#True

