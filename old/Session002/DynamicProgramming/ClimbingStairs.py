class Solution:
    """
    https://leetcode.com/problems/climbing-stairs/
    """
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n==0 or n==1 or n==2:
            return n
        prev_prev_step=1
        prev_step=2
        res=0
        for i in range(2,n):
            res=prev_step+prev_prev_step
            prev_prev_step=prev_step
            prev_step=res
        return res

    def climbStairs2(self, n):
        dp=[0]*(n+1)
        dp[1]=1
        dp[2]=2
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]


if __name__=="__main__":
    c=Solution()
    print(c.climbStairs2(2))
    print(c.climbStairs2(3))
