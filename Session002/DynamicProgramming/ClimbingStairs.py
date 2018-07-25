class Solution:
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

if __name__=="__main__":
    c=Solution()
    print(c.climbStairs(2))
    print(c.climbStairs(3))
