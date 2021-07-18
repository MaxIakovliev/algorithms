class Solution:
    """
    https://leetcode.com/problems/wiggle-subsequence/

    solution:
    https://leetcode.com/problems/wiggle-subsequence/discuss/84843/Easy-understanding-DP-solution-with-O(n)-Java-version
    """
    def wiggleMaxLength(self, nums: 'List[int]') -> int:
        n=len(nums)
        if n==0:
            return 0
        up=[0 for _ in range(n)]
        down=[0 for _ in range(n)]
        up[0]=1
        down[0]=1
        for i in range(1,n):
            if nums[i]>nums[i-1]:
                up[i]=down[i-1]+1
                down[i]=down[i-1]
            elif nums[i]<nums[i-1]:
                down[i]=up[i-1]+1
                up[i]=up[i-1]
            else:
                down[i]=down[i-1]
                up[i]=up[i-1]
        return max(down[-1],up[-1])

        