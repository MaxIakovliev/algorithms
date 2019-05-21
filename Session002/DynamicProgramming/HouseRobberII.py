class Solution:
    """
    https://leetcode.com/problems/house-robber-ii/
    solution:
    https://leetcode.com/problems/house-robber-ii/discuss/290433/java-code%3ARuntime%3A-0-ms-faster-than-100.00.-Memory-Usage%3A-33.3-MB-less-than-100.00
    """
    def rob(self, nums: 'List[int]') -> 'int':
        if len(nums)==0:
            return 0
        if len(nums)==1:
            return nums[-1]
        dp1=[-1 for i in range(len(nums)+1)]
        dp1[0]=0
        dp1[1]=nums[0]
        for i in range(2, len(nums)):
            dp1[i]=max(dp1[i-2]+nums[i-1], dp1[i-1])
        
        dp2=[-1 for i in range(len(nums)+1)]
        dp2[0]=0
        dp2[1]=0
        for i in range(2, len(nums)+1):
            dp2[i]=max(dp2[i-2]+nums[i-1], dp2[i-1])
        
        return max(dp1[-2], dp2[-1])

if __name__ == "__main__":
    c=Solution()
    print(c.rob([2,3,2])) #3
    print(c.rob([1,2,3,1])) #4
    print(c.rob([4,1,2])) #4
            


            
            
        