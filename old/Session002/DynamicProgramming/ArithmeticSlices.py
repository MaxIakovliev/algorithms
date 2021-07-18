class Solution:
    """
    https://leetcode.com/problems/arithmetic-slices/
    """
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        if len(A)<3:
            return 0
        dp=[0]*len(A)
        res=0
        for i in range(2,len(A)):
            if A[i]-A[i-1]==A[i-1]-A[i-2]:
                dp[i]=dp[i-1]+1
            else:
                dp[i]=0
            res+=dp[i]
        return res
        